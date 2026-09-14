# Book Store

یک وب‌اپلیکیشن فروشگاه کتاب ساخته‌شده با Django که امکان مدیریت، نمایش و [خرید/رزرو] کتاب‌ها را از طریق یک پنل ادمین کامل فراهم می‌کند. [یک جمله کوتاه دیگر درباره هدف پروژه — مثلاً: "کاربران می‌توانند کتاب‌ها را مرور کرده و ادمین از طریق پنل مدیریت، موجودی و اطلاعات کتاب‌ها را کنترل می‌کند."]

## دمو زنده

🔗 [مشاهده نسخه آنلاین](https://your-project.up.railway.app)

## امکانات

- [ ] نمایش لیست کتاب‌ها با جزئیات (عنوان، نویسنده، قیمت، موجودی)
- [ ] پنل ادمین کامل برای مدیریت کتاب‌ها

## تکنولوژی‌ها

- Python / Django
- PostgreSQL (Production) / SQLite (Development)
- Gunicorn (سرور Production)
- WhiteNoise (سرو فایل‌های استاتیک)
- python-decouple / dj-database-url (مدیریت تنظیمات و اتصال دیتابیس)
- دیپلوی روی Railway

## پیش‌نیازها

- Python 3.10 یا بالاتر
- pip

## نصب و اجرا (محلی)

# کلون کردن مخزن
git clone https://github.com/mmdparimoon/Book-Store.git
cd Book-Store

# ساخت و فعال‌سازی محیط مجازی
python -m venv .venv
source .venv/Scripts/activate      # ویندوز (Git Bash)
# یا: .venv\Scripts\activate       # ویندوز (CMD/PowerShell)

# نصب پکیج‌ها
pip install -r requirements.txt

# تنظیم متغیرهای محیطی
cp .env.example .env
# سپس مقادیر داخل .env را با اطلاعات واقعی پر کن (مثلاً SECRET_KEY)

# اجرای مایگریشن‌ها
python manage.py migrate

# ساخت کاربر ادمین (اختیاری)
python manage.py createsuperuser

# اجرای سرور توسعه
python manage.py runserver
سپس در مرورگر به آدرس زیر برو:
http://127.0.0.1:8000/
برای دسترسی به پنل ادمین:
http://127.0.0.1:8000/admin/
## متغیرهای محیطی

فایل .env باید شامل موارد زیر باشد (نمونه در .env.example):

SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
## دیپلوی (Deployment)

این پروژه روی [Railway](https://railway.app) با PostgreSQL دیپلوی شده است. برای دیپلوی نسخه خودتان:

1. یک مخزن PostgreSQL در Railway بسازید.
2. متغیرهای محیطی زیر را تنظیم کنید: SECRET_KEY, DEBUG=False, DATABASE_URL, CSRF_TRUSTED_ORIGINS
3. فایل Procfile شامل دستورات build و اجرای gunicorn است.

## ساختار پروژه

Book-Store/
├── [نام پوشه تنظیمات اصلی]/   # تنظیمات پروژه (settings, urls, wsgi)
├── [نام اپ اصلی]/              # اپلیکیشن مدیریت کتاب‌ها
├── .env.example                # نمونه متغیرهای محیطی مورد نیاز
├── Procfile                    # دستورات اجرا برای دیپلوی
├── requirements.txt            # وابستگی‌های پروژه
└── manage.py

## نویسنده

Mohammad Parimoon — [لینک گیت‌هاب یا لینکدین]
