from celery import shared_task
from django.core.mail import send_mail
from core.settings import DEFAULT_FROM_EMAIL


@shared_task
def send_email_async(user_email, reset_link, user_name):
    send_mail(
        subject="Password Reset Request",
        message=f"Click the link to reset your password: {reset_link}",
        from_email=DEFAULT_FROM_EMAIL,
        recipient_list=[user_email],
        fail_silently=False,
        html_message=f"""
    <html>
        <body>
            <p>Hello {user_name},</p>
            <p>We received a request to reset your password.</p>
            <p>
                <a href="{reset_link}">Click here to reset your password</a>
            </p>
            <p>This link is valid for 10 minutes.</p>
            <p>If you didn't request this, please ignore this email.</p>
        </body>
    </html>
    """,
    )
