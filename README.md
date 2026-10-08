# WADP-L4 Demonstration-6 [Product-Management-System]
# 🛒 Product Management System

A simple **Product Management Web Application** built with **Python and Django**.

This project allows authenticated users to manage products by adding product information such as name, category, description, image, price, quantity, production date, and total amount.

The project demonstrates practical Django concepts including **Custom User Models, Authentication, CRUD Operations, Foreign Key Relationships, Image Uploads, Forms, Templates, and Database Management**.

---

## 🚀 Features

### 👤 User Management

* Custom User Model using Django `AbstractUser`
* User registration and login
* Full name support
* Phone number support
* Authentication-based product management

### 📦 Product Management

* Add new products
* View product information
* Update products
* Delete products
* Manage product quantity
* Set product price
* Add product descriptions
* Upload product images
* Set production date

### 🏷️ Product Categories

Products can be organized into different categories:

* 🥬 Vegetable
* 🐟 Fishes
* 🍎 Fruits

### 💰 Product Pricing

The application supports:

* Product price
* Product quantity
* Total amount

### 🖼️ Product Images

Users can upload product images using Django's `ImageField`.

---

## 🛠️ Technologies Used

* **Python**
* **Django**
* **SQLite**
* **HTML5**
* **CSS3**
* **Bootstrap** *(if used in the project)*
* **Django Templates**
* **Git & GitHub**

---

## 🔗 Database Relationship

Each product is associated with a user through a **Foreign Key**.

```text
ProductUserModel
       │
       │  One-to-Many
       ↓
ProductModel
       │
       ├── Name
       ├── Description
       ├── Category
       ├── Image
       ├── Price
       ├── Quantity
       ├── Total Amount
       └── Production Date
```

The relationship is created using:

```python
created_by = models.ForeignKey(
    ProductUserModel,
    on_delete=models.CASCADE,
    related_name='products',
    null=True
)
```

Because of `related_name='products'`, a user's products can be accessed with:

```python
request.user.products.all()
```

---

## 📂 Project Structure

```text
Product Management/
│
├── manage.py
│
├── project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── ProductApp/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── media/
│   └── product/
│
├── static/
│
├── db.sqlite3
└── manage.py
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository.git
```

### 2. Navigate to the Project

```bash
cd your-repository
```

### 3. Create a Virtual Environment

```bash
python -m venv env
```

### 4. Activate Virtual Environment

**Windows:**

```bash
env\Scripts\activate
```

**Mac/Linux:**

```bash
source env/bin/activate
```

### 5. Install Dependencies

```bash
pip install django pillow
```

Or, if your project contains a `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configure Custom User Model

Since the project uses `ProductUserModel`, add the custom user model to `settings.py`:

```python
AUTH_USER_MODEL = 'ProductApp.ProductUserModel'
```

Replace `ProductApp` with your actual Django app name.

---

## 🗄️ Database Setup

Create migrations:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

Create a superuser:

```bash
python manage.py createsuperuser
```

---

## ▶️ Run the Project

Start the Django development server:

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

---

## 🔐 Django Admin

Access the Django administration panel:

```text
http://127.0.0.1:8000/admin/
```

From the admin panel, you can manage:

* Users
* Products
* Categories
* Prices
* Quantities
* Production dates
* Product images

---

## 📋 Product Fields

| Field           | Description                  |
| --------------- | ---------------------------- |
| Name            | Product name                 |
| Description     | Product details              |
| Category        | Vegetable, Fishes, or Fruits |
| Image           | Product image                |
| Price           | Price of the product         |
| Quantity        | Available product quantity   |
| Total Amount    | Total product value          |
| Production Date | Product production date      |
| Created By      | User who created the product |
| Created At      | User creation information    |

---

## 💡 Example Products

| Product    | Category  |  Price | Quantity |
| ---------- | --------- | -----: | -------: |
| Potato     | Vegetable |  50.00 |       20 |
| Hilsa Fish | Fishes    | 850.00 |        5 |
| Mango      | Fruits    | 120.00 |       15 |

---

## 🔄 Product Management Workflow

```text
Register / Login
       ↓
Create Product
       ↓
Add Product Details
       ↓
Select Category
       ↓
Set Price & Quantity
       ↓
Upload Product Image
       ↓
Save Product
       ↓
View / Update / Delete
```

---

## 🎯 Learning Objectives

This project demonstrates practical knowledge of:

* Python
* Django
* `AbstractUser`
* Custom User Models
* Django Authentication
* Django Models
* CRUD Operations
* Foreign Key Relationships
* `related_name`
* Django Forms
* Django Templates
* Image Upload
* Media Files
* SQLite Database
* Django Admin
* Git & GitHub

---

## 🔮 Future Improvements

Possible future features include:

* 🔎 Product search
* 🔍 Category filtering
* 📊 Product dashboard
* 📦 Stock management
* 🛒 Shopping cart
* 💳 Online payment
* 🧾 Invoice generation
* 📱 Responsive UI
* 📈 Sales reports
* 🔔 Low-stock notifications
* 🔐 Password reset
* 🚀 Deployment with Render or PythonAnywhere

---

## 👨‍💻 Developer

**Oren Michael Dessai**

### 💻 Backend Development Focus

**Python | Django | Backend Development | REST APIs**

Building web applications with Django and continuously improving backend development skills.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project was created for **learning and educational purposes**.
