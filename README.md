
# MicroApp Project

This is a full-stack web application with a Flask backend, React frontend, and PostgreSQL database. It includes Docker and Kubernetes setup with automatic database migrations on startup.

## Project Structure

```
project/
├── backend/
│   ├── app/
│   │   └── main.py
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.js
│   │   └── index.js
│   ├── Dockerfile
│   └── nginx.conf
├── postgres/
│   └── init.sql
├── helm/
│   ├── backend/
│   │   ├── Chart.yaml
│   │   ├── values.yaml
│   │   └── templates/
│   │       ├── deployment.yaml
│   │       ├── service.yaml
│   │       └── hpa.yaml
│   ├── frontend/
│   │   ├── Chart.yaml
│   │   ├── values.yaml
│   │   └── templates/
│   │       ├── deployment.yaml
│   │       └── service.yaml
│   └── postgres/
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
│           ├── deployment.yaml
│           └── service.yaml
├── ingress/
│   └── ingress.yaml
├── certs/
│   ├── tls.crt
│   └── tls.key
├── .github/
│   └── workflows/
│       └── deploy.yml
└── README.md

```

## Prerequisites

To run this project locally, ensure you have the following installed:

- Docker & Docker Compose
- Kubernetes (if using Kubernetes)
- Helm (if using Helm)
- Node.js (for React development)
- Python 3 (for Flask backend development)

## Installation

### 1. Clone the repository:

```bash
git clone <repository-url>
cd microapp-k8s-cicd
```

#### a. Set up the Kubernetes environment:

- Create the required namespaces and resources.
- Deploy your services using Helm.

```bash
helm install microapp ./helm
```

This will deploy the backend, frontend, and PostgreSQL services, along with Ingress controllers for routing.

#### b. Access the app on Kubernetes:

If you have Ingress set up, the app should be accessible at the configured URL.

```bash
kubectl get ingress
```

## Flask Backend

The Flask application is located in the `backend/` directory and provides the following features:

- **Database Connection**: Connects to PostgreSQL to interact with the `microapp` database.
- **Products API**: Provides an endpoint to get product data from the database.

### Endpoints:
- **GET `/products`**: Fetches the list of products stored in the database.

### How it Works:

The Flask app connects to a PostgreSQL database using the `psycopg2` library. The database initialization and migrations are handled through the `migrations.sql` file, which is automatically executed during the container setup.

## React Frontend

The React app, located in the `frontend/` directory, displays product data fetched from the Flask API.

### Features:
- Displays a list of products with name and price.
- Reacts to the data returned by the Flask API.

### Running the Frontend:
- The frontend runs on `http://localhost:3000`.
## PostgreSQL Database

The PostgreSQL database runs in a Docker container.


## Helm Setup (Optional)

### Helm Chart Configuration:

If you're deploying to Kubernetes using Helm, follow the Helm configuration and values in the `helm/` directory. You can deploy the app to a Kubernetes cluster using the Helm command:

```bash
helm install microapp ./helm
```

Make sure the appropriate values are set in the `values.yaml` file, such as the correct database connection string, service ports, and ingress configuration.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
