from django.shortcuts import render

# Create your views here.
import requests
from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Listing, Booking, Review, Payment
from .serializers import ListingSerializer, BookingSerializer, ReviewSerializer
#from .serializers import PaymentSerializer



class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    
    
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    
    

class PaymentViewSet(viewsets.ViewSet):
    def initiate_payment(self, request, booking_id):
        try:
            booking = Booking.objects.get(id=booking_id)
        except Booking.DoesNotExist:
            return Response({"error": "Booking not found"}, status=status.HTTP_404_NOT_FOUND)

        data = {
            "amount": str(booking.total_price),
            "currency": "ETB",
            "email": booking.user.email,
            "first_name": booking.user.first_name,
            "last_name": booking.user.last_name,
            "tx_ref": f"booking_{booking.id}",
            "callback_url": "https://yourdomain.com/payment/callback"
        }

        headers = {
            "Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"
        }

        response = requests.post(f"{settings.CHAPA_API_BASE_URL}/transaction/initialize", json=data, headers=headers)
        chapa_response = response.json()

        if response.status_code == 200 and chapa_response.get("status") == "success":
            payment = Payment.objects.create(
                booking=booking,
                amount=booking.total_price,
                transaction_id=chapa_response["data"]["tx_ref"],
                status="Pending"
            )
            return Response({"payment_url": chapa_response["data"]["checkout_url"]})
        return Response({"error": chapa_response.get("message", "Payment initiation failed")}, status=400)

    def verify_payment(self, request, tx_ref):
        headers = {
            "Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"
        }
        response = requests.get(f"{settings.CHAPA_API_BASE_URL}/transaction/verify/{tx_ref}", headers=headers)
        chapa_response = response.json()

        try:
            payment = Payment.objects.get(transaction_id=tx_ref)
        except Payment.DoesNotExist:
            return Response({"error": "Payment record not found"}, status=404)

        if chapa_response.get("status") == "success" and chapa_response["data"]["status"] == "success":
            payment.status = "Completed"
        else:
            payment.status = "Failed"
        payment.save()

        return Response({"status": payment.status})
