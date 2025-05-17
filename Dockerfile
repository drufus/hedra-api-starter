FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install uv (Python package manager)
RUN pip install uv

# Copy all project files into the container
COPY . .

# Install dependencies from pyproject.toml
RUN uv sync

# Set default command (can override in Coolify job)
CMD ["uv", "--version"]
