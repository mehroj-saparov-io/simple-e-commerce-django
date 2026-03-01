
# Simple E-Commerce Django

Simple E-Commerce Django – bu Django va PostgreSQL asosida yaratilgan oddiy onlayn do‘kon loyihasi.  
Loyihada foydalanuvchi ro‘yxatdan o‘tishi, login/logout, mahsulotlarni ko‘rishi, savatga qo‘shishi va buyurtma berishi mumkin.

![YouTube Video Banner](https://github.com/mehroj-saparov-io/simple-e-commerce-django/blob/main/static/images/banner.png)

🎥 YouTube video: [Simple E-Commerce Django – Loyihani ko‘rish](https://youtu.be/DYj0IBZnjoo?si=wDhfms7CWo6k-_KI)

## 🛠 Texnologiyalar
- **Python 3.13**
- **Django 5.2**
- **PostgreSQL**
- **HTML, CSS (basic)**

## 📂 Loyihani tuzilishi
```

simple-e-commerce-django/
├─ apps/
│  ├─ accounts/      # Foydalanuvchi authentication
│  ├─ products/      # Mahsulotlar list va detail
│  ├─ cart/          # Savat funksiyalari
│  ├─ orders/        # Buyurtma va checkout
├─ core/             # Django project settings va URLs
├─ media/            # Uploaded files
├─ templates/        # HTML templates
├─ static/           # Static files
└─ manage.py

````

## ⚙️ Funksionallik
1. **Accounts**
   - Ro‘yxatdan o‘tish (register)
   - Login va Logout
2. **Products**
   - Mahsulotlar ro‘yxati
   - Mahsulot detallari
3. **Cart**
   - Mahsulotni savatga qo‘shish
   - Savatni ko‘rish, yangilash, o‘chirish
4. **Orders**
   - Checkout
   - Order success sahifasi

## 🚀 Loyihani ishga tushurish
1. Repository’ni klonlash:
```bash
git clone https://github.com/mehroj-saparov-io/simple-e-commerce-django
cd simple-e-commerce-django
````

2. Virtual muhit yaratish:

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

3. Talab qilinadigan paketlarni o‘rnatish:

```bash
pip install -r requirements.txt
```

4. PostgreSQL database yaratish

5. Django migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Superuser yaratish:

```bash
python manage.py createsuperuser
```

7. Serverni ishga tushurish:

```bash
python manage.py runserver
```

8. Brauzerda ochish:

```
http://127.0.0.1:8000/
```

## 🔧 Admin panel

* URL: `/admin/`
* Superuser orqali kirib, mahsulotlar, buyurtmalar va foydalanuvchilarni boshqarish mumkin.

## 📌 Eslatma

* Media fayllar `MEDIA_URL` va `MEDIA_ROOT` orqali saqlanadi.
* Accounts URL’lari `/accounts/` prefix bilan ishlaydi (`login/`, `register/`).

## 👤 Muallif

* Mehroj Saparov
