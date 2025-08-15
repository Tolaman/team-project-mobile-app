from django.urls import path
from . import views

urlpatterns = [
  path('reports/', views.ReportListView.as_view(), name='report-list'),
  path('reports/delete/<int:pk>/', views.ReportDelete.as_view(), name='delete-report'),
]
