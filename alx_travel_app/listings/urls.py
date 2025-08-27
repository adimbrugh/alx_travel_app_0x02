

from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, BookingViewSet, ReviewViewSet, InitiatePaymentView
from django.urls import path, include



router = DefaultRouter()
router.register(r'listing', ListingViewSet)
router.register(r'booking', BookingViewSet)
router.register(r'reviews', ReviewViewSet)  # Added ReviewViewSet


payment_view = InitiatePaymentView.as_view({'post': 'initiate_payment'})
verify_view = InitiatePaymentView.as_view({'get': 'verify_payment'})


urlpatterns = [
    path('', include(router.urls)),
    path('payment/initiate/<int:booking_id>/', payment_view, name='initiate-payment'),
    path('payment/verify/<str:tx_ref>/', verify_view, name='verify-payment'),
]
