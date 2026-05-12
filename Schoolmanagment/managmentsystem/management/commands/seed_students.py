from django.core.management.base import BaseCommand
from managmentsystem.models import Student
from django.core.files.base import ContentFile
import random

class Command(BaseCommand):
    help = "Seed database with 20 students"

    def handle(self, *args, **kwargs):

        students_data = [
            {
                "name": "Aman Sharma",
                "student_class": "10th",
                    "city": "Delhi",
                    "age": 15,
                    "address": "Street 1, Delhi",
                    "roll_no": "R001",
                    "email": "aman.sharma@gmail.com"
            },
            {
                "name": "Rahul Verma",
                "student_class": "9th",
                    "city": "Mumbai",
                    "age": 14,
                    "address": "Street 2, Mumbai",
                    "roll_no": "R002",
                    "email": "rahul.verma@gmail.com"
            },
            {
                "name": "Priya Singh",
                "student_class": "8th",
                    "city": "Lucknow",
                    "age": 13,
                    "address": "Street 3, Lucknow",
                    "roll_no": "R003",
                    "email": "priya.singh@gmail.com"
            },
            {
                "name": "Neha Gupta",
                "student_class": "11th",
                    "city": "Jaipur",
                    "age": 16,
                    "address": "Street 4, Jaipur",
                    "roll_no": "R004",
                    "email": "neha.gupta@gmail.com"
            },
            {
                "name": "Rohit Kumar",
                "student_class": "12th",
                    "city": "Patna",
                    "age": 17,
                    "address": "Street 5, Patna",
                    "roll_no": "R005",
                    "email": "rohit.kumar@gmail.com"
            },
            {
                "name": "Simran Kaur",
                "student_class": "7th",
                    "city": "Amritsar",
                    "age": 12,
                    "address": "Street 6, Amritsar",
                    "roll_no": "R006",
                    "email": "simran.kaur@gmail.com"
            },
            {
                "name": "Karan Mehta",
                "student_class": "10th",
                    "city": "Chandigarh",
                    "age": 15,
                    "address": "Street 7, Chandigarh",
                    "roll_no": "R007",
                    "email": "karan.mehta@gmail.com"
            },
            {
                "name": "Anjali Yadav",
                "student_class": "9th",
                    "city": "Kanpur",
                    "age": 14,
                    "address": "Street 8, Kanpur",
                    "roll_no": "R008",
                    "email": "anjali.yadav@gmail.com"
            },
            {
                "name": "Vikas Sharma",
                "student_class": "8th",
                    "city": "Agra",
                    "age": 13,
                    "address": "Street 9, Agra",
                    "roll_no": "R009",
                    "email": "vikas.sharma@gmail.com"
            },
            {
                "name": "Pooja Mishra",
                "student_class": "11th",
                    "city": "Bhopal",
                    "age": 16,
                    "address": "Street 10, Bhopal",
                    "roll_no": "R010",
                    "email": "pooja.mishra@gmail.com"
            },
            {
                "name": "Arjun Patel",
                "student_class": "12th",
                    "city": "Ahmedabad",
                    "age": 17,
                    "address": "Street 11, Ahmedabad",
                    "roll_no": "R011",
                    "email": "arjun.patel@gmail.com"
            },
            {
                "name": "Sneha Joshi",
                "student_class": "7th",
                    "city": "Pune",
                    "age": 12,
                    "address": "Street 12, Pune",
                    "roll_no": "R012",
                    "email": "sneha.joshi@gmail.com"
            },
            {
                "name": "Deepak Roy",
                "student_class": "10th",
                    "city": "Kolkata",
                    "age": 15,
                    "address": "Street 13, Kolkata",
                    "roll_no": "R013",
                    "email": "deepak.roy@gmail.com"
            },
            {
                "name": "Meera Das",
                "student_class": "9th",
                    "city": "Guwahati",
                    "age": 14,
                    "address": "Street 14, Guwahati",
                    "roll_no": "R014",
                    "email": "meera.das@gmail.com"
            },
            {
                "name": "Sahil Khan",
                "student_class": "8th",
                    "city": "Hyderabad",
                    "age": 13,
                    "address": "Street 15, Hyderabad",
                    "roll_no": "R015",
                    "email": "sahil.khan@gmail.com"
            },
            {
                "name": "Riya Kapoor",
                "student_class": "11th",
                    "city": "Noida",
                    "age": 16,
                    "address": "Street 16, Noida",
                    "roll_no": "R016",
                    "email": "riya.kapoor@gmail.com"
            },
            {
                "name": "Yash Thakur",
                "student_class": "12th",
                    "city": "Indore",
                    "age": 17,
                    "address": "Street 17, Indore",
                    "roll_no": "R017",
                    "email": "yash.thakur@gmail.com"
            },
            {
                "name": "Tina Arora",
                "student_class": "7th",
                    "city": "Ludhiana",
                    "age": 12,
                    "address": "Street 18, Ludhiana",
                    "roll_no": "R018",
                    "email": "tina.arora@gmail.com"
            },
            {
                "name": "Mohit Jain",
                "student_class": "10th",
                    "city": "Surat",
                    "age": 15,
                    "address": "Street 19, Surat",
                    "roll_no": "R019",
                    "email": "mohit.jain@gmail.com"
            },
            {
                "name": "Kavya Rani",
                "student_class": "9th",
                    "city": "Varanasi",
                    "age": 14,
                    "address": "Street 20, Varanasi",
                    "roll_no": "R020",
                    "email": "kavya.rani@gmail.com"
            },
        ]

        for data in students_data:

            student, created = Student.objects.update_or_create(
                roll_no=data["roll_no"],
                defaults={
                    "name": data["name"],
                    "student_class": data["student_class"],
                    "city": data["city"],
                    "age": data["age"],
                    "address": data["address"],
                    "email": data["email"],
                }
            )

            # Add dummy image
            if created or not student.image:
                student.image.save(
                    f"{student.roll_no}.jpg",
                    ContentFile(b""),
                    save=True
                )

        self.stdout.write(
            self.style.SUCCESS("20 Students Seeded/Updated Successfully!")
        )
