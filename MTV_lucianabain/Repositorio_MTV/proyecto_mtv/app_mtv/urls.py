from xml.etree.ElementInclude import include
from django.urls import path


urlpatterns = [
    path('app_mtv/', include('app_mtv.urls'))
]