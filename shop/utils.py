from random import Random

from ArcDeco.settings import EMAIL_FROM  # Импорт smtp

from django.contrib.auth.models import User

from django.core.mail import send_mail  # Импорт и отправка почты


def generate_random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars)-1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type="register"):
    email_record = User()  # instantiate
    random_str = generate_random_str(16)  # взять случайное число
    email_record.code = random_str
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    if send_type == "register":
        email_title = "Ссылка для активации регистрации"
        email_body = "Пожалуйста, нажмите на ссылку ниже, чтобы активировать свою учетную запись: http://127.0.0.1:8000/active/-199081".format(
            random_str)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
