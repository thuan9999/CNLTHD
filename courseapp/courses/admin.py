from django.contrib import admin
from .models import Category, Course, Lesson, Tag
from  django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    search_fields = ['name']
    list_filter = ['name']


class CourseForm(forms.ModelForm):
    description = forms.CharField(widget= CKEditorUploadingWidget)

    class Meta:
        model =Course
        fields ='__all__' 


class TagInLineAdmin(admin.StackedInline):
    model = Course.tags.through


class CourseAdmin(admin.ModelAdmin):
    list_display =['pk', 'subject', 'created_date','updated_date', 'category','active']
    readonly_fields=['img']
    inlines =[TagInLineAdmin]
    form = CourseForm


class CourseAppAdminSite(admin.AdminSite):
    site_header='HE THONG QUAN LY KHOA HOC'


    def  img(self, course): 
        if course:
            return mark_safe(
                '<img src="/static/{url}" width="120" />'\
                .format(url=course.image.name)
            )
        

    class Media:
        css = {
            'all': ('/static/css/style.css', )
        }



admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
admin.site.register(Tag)
admin.site =CourseAppAdminSite('mycourse')

# Register your models here.
