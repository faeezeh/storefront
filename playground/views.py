# from django.core.mail import mail_admins,EmailMessage,send_mail,BadHeaderError
from django.shortcuts import render
# from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers

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

    notify_customers.delay('hello')
    return render(request, 'hello.html', {'name': 'Faezeh'})

    
