Step 1:- Run This Command For Installing Virtual Enviroment (python -m venv myenv)

Step 2:- Run THis COmmand For Activation 
         For Windows (myenv\Scripts\activate)
         For Mac/Linux(source myenv/bin/activate)

Step 3:- Now HAve To INstall Django (pip install django)
Step 4:- Now Run (pip install pscopyg2)

Step 5:- Now Run Two Command 
         (python manage.py makemigrations)
         (python manage.py migrate)

Step 6:- Run This Command For Image Storage 
         (pip install pillow)

Step 7:- Create Super User
         (python manage.py createsuperuser)

Step 8:- Create A Model Of Students

Step 9:- Create URLS And VIEWS File 

Step 10:- Create HTML Pages For Froontend To Represent All The Data And Performe CRUD Operation  

Step 11:- Create a Seed File 
        (App)     students/
                  │
                  ├── management/
                  │   ├── __init__.py
                  │   └── commands/
                  │       ├── __init__.py
                  │       └── seed_students.py

         students/management/commands/seed_students.py

         Enter Student Seeded data

Step 12:- Run Migrations First
            python manage.py makemigrations
            python manage.py migrate

Step 13:- Run Seeder Command
            python manage.py seed_students

Step 14:- Add a serching where we can search using name , rool no , city , class 
            Updating View.py and HTML File

Step 15:- Adding Filter And Paginator
         Updating View.py and HTML File

There are two types of button 
     Form Button => By using This Button We can store some data Usually this button is uing in a form
        example:- <button type="submit" class="btn btn-success">Add Student</button>

     Redirect Button => By Using This Button We can redirect on any web page.
        examplle:- <a class="btn btn-outline-light me-2" href="{% url 'student_list' %}">Home</a>

Step 16:- Making  A Function To Send Test Email 
          Make Changes in settings.py,views.py,url.py and make a HTML Fie Of Email Sent Messaage 

Step 17:- Settings.py
        # Email settings
        EMAIL_HOST = 'smtp.gmail.com'
        EMAIL_PORT = 587
        EMAIL_HOST_USER = 'tridevx9@gmail.com'
        EMAIL_HOST_PASSWORD = 'ngwf ojdy iyde rlrx'
        EMAIL_USE_TLS = True

Step 18:- App (views.py)
          # 📌 SEND TEST EMAIL
        def send_test_email(request):
                subject = 'Test Email'
                message = 'This is a test email sent from Django.'
                from_email = 'tridevx9@gmail.com'
                      recipient_list = ['geuvizegebre-9696@yopmail.com']  # Replace with actual recipient email

                try:
                         send_mail(subject, message, from_email, recipient_list)
                         return render(request, 'email_sent.html', {'message': 'Test email sent successfully!'})
                         except Exception as e:
                            return render(request, 'email_sent.html', {'message': f'Error sending email: {str(e)}'})

Step 19:- App(urls.py)
        from django.urls import path
        # from . import views
        from .views import *

urlpatterns = [
    path('students/', student_list, name='student_list'),
    path('add/', add_student, name='add_student'),
    path('update/<int:id>/', update_student, name='update_student'),
    path('delete/<int:id>/', delete_student, name='delete_student'),
    path('send-test-email/', send_test_email, name='send_test_email'),
]

Step 20:- Make a HTML File Which Will Be Email_Seent.html

