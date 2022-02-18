from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from myshop import views

# urlpatterns = [
#     path("myshop/", include("myshop.urls")),
#     path("admin/", admin.site.urls),
# ]


router = routers.DefaultRouter()
router.register(r"item", views.ItemView, "item")
router.register(r"product", views.ProductView, "product")
router.register(r"sale", views.SaleView, "sale")
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("auth/", obtain_auth_token),
]
