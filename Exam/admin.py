from django.contrib import admin
from .models import Student, Room, Course, Exam
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(Student)
class StudentSAdmin(ImportExportModelAdmin):
    list_display = (
        'std_Id',
        'firstName',
        'lastName',
    )


@admin.register(Course)
class ExamAdmin(admin.ModelAdmin):
    list_display = (
        'courseName',
        'course_Id',
    )


@admin.register(Room)
class ExamAdmin(admin.ModelAdmin):
    list_display = (
        'roomName',
        'floor',
        'seats',
    )


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = (
        'course',
        'students',
        'rooms',
        'seats',
        'floor',
        'program',
        'date',
        'time',
    )
