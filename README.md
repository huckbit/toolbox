# 🛠️ Workshop Inventory Tracker (WIP)

A simple API to keep track of a workshop tool inventory, maintenance notes, and future tool wishlists. This is a personal project currently under active development.

## Project Status: Work in Progress 🚧
This repository is a sandbox for testing out backend structures and local container orchestration. It is not intended for production use just yet.

## Prerequisites
You will need the following installed to run the app locally:
*   **OrbStack** or **Docker Desktop**
*   **Git**

## Quick Start (Local Development)

1.  **Clone the repository**
    ```bash
    git clone <https://github.com/huckbit/toolbox.git>
    cd toolbox
    ```

2.  **Configure Environment Variables**
    Create a `.env` file in the root directory. You can use the following as a template:
    ```plaintext
    POSTGRES_DB=toolbox
    POSTGRES_USER=admin
    POSTGRES_PASSWORD=password123
    ```

3.  **Start the environment**
    Run the following command to build the image and start the database:
    ```bash
    docker compose up --build
    ```

## How to use the API
Once the containers are running, you can interact with the inventory through the browser:

*   **Interactive API Docs**: Navigate to `http://localhost:8000/docs` to add or view tools via the Swagger UI.
*   **Tool List (JSON)**: View the full inventory at `http://localhost:8000/tools/`.

## Running Tests
To run the automated test suite and ensure everything is configured correctly:
```bash
docker compose exec web pytest
```