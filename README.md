Here's a **README.md** file for Docker installation and running your **Flask To-Do App**:  

---  

```markdown
# To-Do Flask App - Docker Deployment

This repository contains a simple Flask-based To-Do application containerized using Docker. Follow the instructions below to set up and run the application.

## Prerequisites

Before running the application, ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/) (if using `docker-compose.yml`)

## Installation Steps

### 1. Clone the Repository
```sh
git clone git@github.com:dhruv1345/todo-flask-app-docker-deployment.git
cd todo-flask-app-docker-deployment
```

### 2. Build the Docker Image
```sh
docker build -t todo-flask-app .
```

### 3. Run the Container
```sh
docker run -p 5000:5000 todo-flask-app
```
The application should now be accessible at **http://localhost:5000**.

## Running with Docker Compose (Optional)
If you have `docker-compose.yml`, you can run:
```sh
docker-compose up --build
```

## Stopping the Application
To stop the container:
```sh
docker stop <container_id>
```
Or, if using Docker Compose:
```sh
docker-compose down
```

## License
This project is open-source and available under the MIT License.
```
