# Toolbox app
## 🛠️ The Ultimate Toolbox API

A modern, production-ready REST API built to catalog and manage tools across multiple categories (woodworking, gardening, mechanical, etc.). .

## 🚀 Key Features & DevOps Tech Stack
*   **Backend Framework:** FastAPI (Python 3.12) utilizing Pydantic for robust data validation.
*   **Database:** PostgreSQL integration via SQLAlchemy ORM for permanent data persistence.
*   **Containerization:** Fully dockerized environment utilizing multi-container **Docker Compose** with custom health checks for local development.
*   **CI/CD Pipeline:** Automated testing workflow via **GitHub Actions** that provisions an ephemeral PostgreSQL cloud database to run automated unit tests (`pytest`) on every Pull Request.

![Build Status](https://github.com/huckbit/toolbox/actions/workflows/test.yml/badge.svg)