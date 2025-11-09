# Use a standard Python 3.11 base image
FROM mcr.microsoft.com/devcontainers/python:0-3.11

# Set an environment variable to tell Poetry to create the virtual environment inside the project folder
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

# Install Poetry
RUN pip install poetry

# [Optional] Keep the container running in the background
CMD ["sleep", "infinity"]
