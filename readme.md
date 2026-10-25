# 🚀 FastAPI Modular To-Do Backend

A professional, layered-architecture backend API built with **FastAPI**, **Pydantic**, **SQLAlchemy**, and **MySQL**. Designed for hands-on mastery of robust backend design principles.

---

## 🏗️ Architecture & Flow
This project separates concerns into a clean 3-layer design:
1. **API Layer (`main.py`)**: Handles HTTP routes (`GET`, `POST`, `PUT`, `DELETE`), request parsing, CORS middleware, and error handling (`HTTPException`).
2. **Logic Layer (`task_service.py`)**: Manages core business rules and validations.
3. **Data Layer (`data_manager.py`)**: Interfaces with the MySQL database using SQLAlchemy ORM.

---

## 🛠️ Tech Stack
* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **Validation:** [Pydantic](https://docs.pydantic.dev/)
* **Database ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)
* **Database Engine:** MySQL
* **Server:** Uvicorn

---

## ⚙️ Getting Started & Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name