from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from pharmAPI import views



# router = routers.DefaultRouter()
# router.register(r"users", views.UserViewSet)
# router.register(r"groups", views.GroupViewSet)


urlpatterns = [
    #path("", include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace="rest_framework")),
    path("types/", views.type_list),
    path("types/<int:pk>/", views.types_info),
    path("drugs/", views.drugs_list),
    path("drugs/<int:pk>/", views.drugs_info),
]



urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
