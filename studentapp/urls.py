
from django.contrib import admin
from django.urls import path,include
from .views import recordview,formview,adrecord,deleterecord,editform,editview,backhome,backhomedit,formview2

urlpatterns = [
path('',recordview,name="homepage"),
path('form.html/',formview),
path('addrecord/',adrecord),
path('deleterecord/<int:deleteid>/',deleterecord),
path('editing.html/<int:editid>/',editform),
path('editing.html/<int:editid>/update/',editview),
path('form.html/homepage/',backhome),
path('editing.html/<int:editid>/homepage/',backhomedit),
path('editing.html/<int:editid>/form.html/',formview2),
path('editing.html/<int:editid>/form.html/homepage/',backhomedit)
]
