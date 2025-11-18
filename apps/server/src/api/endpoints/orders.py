import csv
import io

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.dependencies import get_current_user
from src.core.db import get_db
from src.models.order import RawOrder

router = APIRouter()

@router.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload_orders(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    if file.content_type != 'text/csv':
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a CSV.")

    try:
        content = (await file.read()).decode('utf-8')
        csv_reader = csv.DictReader(io.StringIO(content))
        orders_to_load = [RawOrder(payload=row) for row in csv_reader]

        if not orders_to_load:
            raise HTTPException(status_code=400, detail="CSV file is empty or invalid.")

        db.add_all(orders_to_load)
        await db.commit()

        return {"message": f"Successfully uploaded {len(orders_to_load)} orders for {current_user}."}
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred during file processing: {str(e)}")


@router.get("/")
async def get_orders(
    db: AsyncSession = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    result = await db.execute(select(RawOrder).order_by(RawOrder.id.desc()))
    orders = result.scalars().all()
    return orders
