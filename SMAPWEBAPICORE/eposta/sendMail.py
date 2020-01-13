from django.core.mail import send_mail

send_mail(
    Subject,
    Message,
    SendMeMailAddres,  # mail hangi ad ile gitsin
    [],  # gönderilecek mail listesi
    fail_silently=False,
)


# üst kısımdakiler tamamen değişken olmalı
