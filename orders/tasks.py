from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)

    subject = 'Order nr. {}'.format(order_id)
    message = 'Deat {}, \n\nYou have successfuly placed an order. You order id is {}'.format(order.first_name, order.id)

    mail_sent = send_mail(subject, message, 'admin@myshop.com', [order.email])
    return mail_sent
