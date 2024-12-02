# Data Challenge API Project

This API is for managing a ig data migration to a new database system, including an endpoint to manage departments, jobs and hired_employees logs

## Table of Contents
- [Overview](#overview)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview
...

## Getting Started
Instructions for setting up the project locally
Prerequisites:
Installation:

Include clear steps to clone the repository, install dependencies, and configure environment variables.

```
git clone https://github.com/al-khemia/receive_data_api.git
cd receive_data_api
```


## API Endpoints

```
http://localhost:8000/
```


```
GET /
Headers: 
  - Authorization: Bearer <token>
Response:
{"message":"Welcome to Receive Data API"}
```

```
POST /migrate_data
Headers: 
  - Authorization: Bearer <token>
Response:
{
  "id": 1,
  "name": "Product Name",
  "price": 29.99
}
```

Run your api locally
```
uvicorn main:app --reload
```

## Installation
...

## Usage
Assuming you have a file ```requirements.txt```, you culd have a ```dockerfile``` like this:

```
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
```

Then you can build your image from the directory that has your ```dockerfile```. e.g:

```
docker build -t your_image .
```

Run a container based on your image:
```
docker run -d --name your_container -p 8000:8000 your_image
```

Check if the API is working 
```
http://localhost:8000/
```

## Contributing
...

## License
...

## Documentation 

[https://hub.docker.com/r/tiangolo/uvicorn-gunicorn-fastapi](https://hub.docker.com/r/tiangolo/uvicorn-gunicorn-fastapi)