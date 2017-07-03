from django.conf.urls import url, include
from rest_framework import routers
from api.viewsets import NoteViewSet

router = routers.SimpleRouter()

router.register(r'notes', NoteViewSet)

urlpatterns = router.urls