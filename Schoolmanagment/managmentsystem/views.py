from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.mail import send_mail
# 📌 READ (List)
# def student_list(request):
#     students = Student.objects.all()
#     return render(request, 'student_list.html', {'students': students})

# def student_list(request):

#     query = request.GET.get('q')

#     students = Student.objects.all()

#     if query:
#         students = students.filter(
#             Q(name__icontains=query) |
#             Q(roll_no__icontains=query) |
#             Q(city__icontains=query) |
#             Q(student_class__icontains=query)
#         )

#     context = {
#         'students': students
#     }

#     return render(request, 'student_list.html', context)

def student_list(request):

    students = Student.objects.all().order_by('id')

    # SEARCH
    query = request.GET.get('q')

    if query:
        students = students.filter(
            Q(name__icontains=query) |
            Q(student_class__icontains=query) |
            Q(roll_no__icontains=query) |
            Q(city__icontains=query) |
            Q(email__icontains=query)
        )

    # PAGINATION
    paginator = Paginator(students, 5)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {
        'students': page_obj,
        'page_obj': page_obj,
    }

    return render(request, 'student_list.html', context)

# 📌 CREATE
def add_student(request):
    if request.method == "POST":
        student = Student.objects.create(
            name=request.POST.get('name'),
            student_class=request.POST.get('student_class'),
            city=request.POST.get('city'),
            age=request.POST.get('age'),
            address=request.POST.get('address'),
            roll_no=request.POST.get('roll_no'),
            email=request.POST.get('email'),
            image=request.FILES.get('image')
        )
        # Send email
        subject = 'Welcome to School Management System'
        message = f'Hello {student.name},\n\nYou have been successfully registered in our School Management System.\n\nDetails:\nName: {student.name}\nRoll No: {student.roll_no}\nClass: {student.student_class}\n\nThank you!'
        from_email = 'vs2734514@gmail.com'
        recipient_list = [student.email]
        send_mail(subject, message, from_email, recipient_list)
        return redirect('student_list')

    return render(request, 'add_student.html')


# 📌 UPDATE
def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST.get('name')
        student.student_class = request.POST.get('student_class')
        student.city = request.POST.get('city')
        student.age = request.POST.get('age')
        student.address = request.POST.get('address')
        student.roll_no = request.POST.get('roll_no')
        student.email = request.POST.get('email')

        if request.FILES.get('image'):
            student.image = request.FILES.get('image')

        student.save()
        return redirect('student_list')

    return render(request, 'update_student.html', {'student': student})


# 📌 DELETE
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')

# 📌 SEND TEST EMAIL
def send_test_email(request):
    subject = 'Test Email'
    message = 'This is a test email sent from Django.'
    from_email = 'vs2734514@gmail.com'
    recipient_list = ['vs2734514@gmail.com']

    try:
        send_mail(subject, message, from_email, recipient_list)
        return render(request, 'email_sent.html', {'message': 'Test email sent successfully!'})
    except Exception as e:
        return render(request, 'email_sent.html', {'message': f'Error sending email: {str(e)}'})
