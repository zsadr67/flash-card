from django.urls import path

from card import views

urlpatterns = [
    path('create/', views.CreateFlashCardView.as_view(), name='create-card'),
    path('update/<pk>/', views.UpdateFlashCardView.as_view(), name='update-card'),
    path('delete/<pk>/', views.DeleteFlashCardView.as_view(), name='delete-card'),
    path('list/<user_id>/', views.ListFlashCardsView.as_view(), name='list-card'),
]
