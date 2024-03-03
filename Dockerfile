# Use Python 3.9 base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files for installing dependencies
COPY pyproject.toml poetry.lock /app/

# Install poetry
RUN pip install poetry

# Install dependencies
RUN poetry config virtualenvs.create false && poetry install --no-dev

# Copy the entire project directory to the container
COPY . /app
