from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('administracao/', include('administracao.urls')),
    path('api/', include('api.urls')),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/logout/', logout_view.Logout.as_view(), name='logout-list'),
]
