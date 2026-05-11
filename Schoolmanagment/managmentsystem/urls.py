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
