from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from emails.views import ru_index, en_index


urlpatterns = [
    path('', ru_index, name='ru-index'),
    path('en/', en_index, name='en-index'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('emails.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
