import sys
from pathlib import Path

src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from core.db import engine
from models.base import Base
from models.order import RawOrder

def create_tables():
    """Connects to the DB and creates tables defined in Base.metadata if they don't exist."""
    print("--- RUNNING DATABASE SETUP SCRIPT ---")

    with engine.connect() as connection:
        print("[INFO] Connection successful.")
        print("[INFO] Checking for tables...")

        Base.metadata.create_all(bind=connection)

        print("[SUCCESS] Database setup complete. Tables are ensured to exist.")

if __name__ == "__main__":
    create_tables()
