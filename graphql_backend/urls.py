from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from graphene_django.views import GraphQLView
from graphene_file_upload.django import FileUploadGraphQLView

admin.site.site_header = "graphql_backend"
admin.site.site_title = "graphql_backend"
admin.site.index_title = "graphql_backend"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', FileUploadGraphQLView.as_view(graphiql=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)