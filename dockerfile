# Use a python image
FROM python:3.6-slim

# Work directory
WORKDIR /Users/linfante/PycharmProjects/migrate_data_api

# Copy project requirements to container
COPY ./requirements.txt /Users/linfante/PycharmProjects/migrate_data_api/requirements.txt

# Install project dependencies
RUN pip install --no-cache-dir -r /Users/linfante/PycharmProjects/migrate_data_api/requirements.txt

# Copy project files to container
COPY ./app /Users/linfante/PycharmProjects/migrate_data_api/app

# Expose app port
EXPOSE 8000

# Define command to execute the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]