from django.contrib import admin
from .models import Registration, Category, Course

admin.site.register(Registration)
admin.site.register(Category)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("title",)}
