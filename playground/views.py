from django.core.cache import cache
# from django.core.mail import mail_admins,EmailMessage,send_mail,BadHeaderError
from django.shortcuts import render
# from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
import requests
import logging

logger = logging.getLogger(__name__)

class HelloView(APIView):
    def get(self, request):

        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Received the response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httpbin is offline')
        return render(request, 'hello.html', {'name': 'data'})

@cache_page(5 * 60)
def say_hello(request):
     
    #  try:
        # send_mail('subject','message','sfaezehsdgh@gmail.com',['sadeghifaeze94@gmail.com'])
        # mail_admins('subject','message',html_message='message')
        #attaching files
        # message = EmailMessage('subject','message','sfaezehsdgh@gmail.com',['sadeghifaeze94@gmail.com'])
        # message.attach_file('playground/static/images/flowers.jpg')
        # message.send()
        # template emails
    #     message = BaseEmailMessage(
    #         template_name = 'emails/hello.html',
    #         context={'name':'faezeh'}
    #     )
    #     message.send(['faeghe@gmail.com'])
    #  except BadHeaderError:
    #      pass

    # cashing
    # key = 'httpbin_result'
    # if cache.get('httpbin_result') is None:
    #     response = requests.get('https://httpbin.org/delay/2')
    #     data = response.json()
    #     #to store data in the cash
    #     cache.set('httpbin_result',data)

    # response = requests.get('https://httpbin.org/delay/2')
    # data = response.json()
    # return render(request, 'hello.html', {'name': data})
    pass



