from django.urls import path
from .views import EmployeeView, EventsView, challenge, rating
from django.views.static import serve
from actum_back import settings

urlpatterns = [
    path('employee/<int:pk>/', EmployeeView.as_view()),
    path('fonts/<path>', serve, {'document_root': settings.FONT_ROOT}),
    path('images/<path>', serve, {'document_root': settings.IMAGE_ROOT}),
    path('awards/<path>', serve, {'document_root': settings.AWARDS_ROOT}),
    path('team_awards/<path>', serve, {'document_root': settings.TEAM_AWARDS_ROOT}),
    path('multiplicators/<path>', serve, {'document_root': settings.MULT_ROOT}),
    path('last/<path>', serve, {'document_root': settings.LAST_ROOT}),
    path('events/', EventsView.as_view()),
    path('challenges/<r_type>', challenge),
    path('rating/<r_type>', rating),
]
