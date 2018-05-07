from django.core.mail import send_mail
from celery import task
from order.models import Order


@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order_id)
    message = 'Dear {},\n\nYou have successfully placed an order.' \
              'Your order id is {}.'.format(order.order_first_name, order.id)
    mail_sent = send_mail(subject, message, 'murza-30@ya.ru', [order.order_email])
    return mail_sent



