from django.urls import path
from .views import ItemView, CreateCheckoutSessionView, CancelView, SuccessView

urlpatterns = [
    path('item/<int:pk>/', ItemView.as_view(), name='item'),
    path('buy/<int:pk>/', CreateCheckoutSessionView.as_view(), name='buy'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
]
