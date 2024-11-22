from django.contrib import admin

from .models import Question, Module, Document, Identifier

admin.site.register(Question)
admin.site.register(Module)
admin.site.register(Document)
admin.site.register(Identifier)