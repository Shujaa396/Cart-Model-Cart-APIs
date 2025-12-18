
# 🧾 POS Module API – FastAPI + PostgreSQL

A backend API for managing POS module assignments per user using **FastAPI**, **PostgreSQL**, and **JWT Auth**.

---

## 🛠️ Tech Stack
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-FF0000?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-000000?style=for-the-badge&logo=python&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)

---

## 📖 Overview

This project is a backend API system for managing platform modules for users.

- 👤 User management with token-based access (JWT)
- 🧾 Profile module update via PATCH
- 🧩 Module return via GET
- 🛡️ Dummy token protection
- 🧬 PostgreSQL + SQLModel DB connection

---

## ✨ Features

- ✅ Modular route structure
- ✅ GET and PATCH user module endpoint
- ✅ Dummy JWT token handling (admin/user)
- ✅ PostgreSQL connection with SQLModel
- ✅ Fully tested with Swagger & Postman

---

## 📁 Folder Structure

```
pos_module_api/
├── auth/
│   └── jwt_auth.py
├── models/
│   └── user.py
├── routes/
│   └── user_profile.py
├── schemas/
│   └── user_profile.py
├── database.py
├── main.py
├── .env
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pos_module_api.git
cd pos_module_api
```

### 2. Setup Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate    # On Windows
# source venv/bin/activate  # On Linux/Mac
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure .env

```
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/nexus
```

### 5. Run the App

```bash
uvicorn main:app --reload
```

---

## 🧪 API Testing

| Endpoint              | Method | Auth Type      | Description                |
|----------------------|--------|----------------|----------------------------|
| `/ping`              | GET    | None           | Health check               |
| `/user/profile`      | GET    | Bearer Token   | Get current user's module  |
| `/user/profile`      | PATCH  | Bearer Token   | Update current module      |

> Dummy token: `dummy_user_token`

---

## ✅ Project Checklist

- [x] FastAPI project runs
- [x] PostgreSQL connected with SQLModel
- [x] GET and PATCH routes for `/user/profile`
- [x] Swagger and Postman tested
- [x] `.env.example` and README included

---

## 👨‍💻 Author

**Syed Shujaa Hussain**

[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:web.shujaa10@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Shujaa396)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/syed-shujaa-hussain-69113b289)

---

## 🏁 Final Notes

✅ Fully working POS Module API with FastAPI + PostgreSQL  
✅ Uses dummy token auth, modular routes, and proper schemas
