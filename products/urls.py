
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from products.views import ProductListView, ProductDetailSlugView,ProductFeaturedListView
urlpatterns = [
    url(r'^$',ProductListView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$',ProductDetailSlugView.as_view()),
    url(r'^featured/$',ProductFeaturedListView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)