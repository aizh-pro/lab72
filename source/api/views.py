from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet
from django.shortcuts import get_object_or_404
from api.serializers import QuoteCreateSerializer, QuoteUpdateSerializer, QuoteSerializer, \
    VoteCreateSerializer
from webapp.models import Quote, Vote
from .permissions import QuotePermissions

class QuoteViewSet(ModelViewSet):
    permission_classes = [QuotePermissions]

    def get_queryset(self):
        if self.request.method == 'GET' and \
                not self.request.user.has_perm('webapp.quote_view'):
            return Quote.get_moderated()
        return Quote.objects.all()
    

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return QuoteCreateSerializer
        elif self.request.method == 'PUT':
            return QuoteUpdateSerializer
        return QuoteSerializer


class VoteCreateView(APIView):
    def post(self, request):
        vote = VoteCreateSerializer(data=request.data)
        if vote.is_valid():
            vote.save()
        return Response(status=201)

    # def create(self, request,pk):
    #     quote = get_object_or_404(Quote, pk=pk)
    #     slr = VoteSerializer(data=request.data, context={'request': request})
    #     if slr.is_valid():
    #         vote = Vote.objects.create(session_key=self.request.session.session_key, quote=quote, rating=1)
    #         return Response(slr.data)
    #     else:
    #         return Response(slr.errors, status=400)


    # def create(self, request):
    #     try:
    #         quote = Quote.objects.get(request.pk)
    #         vote = Vote.objects.create(session_key=self.request.session.session_key, quote=quote, rating=1)
    #         slr = VoteSerializer(vote)
    #         return JsonResponse({'quote': slr.data}, safe=False)
    #     except Exception:
    #         return JsonResponse({'error':"Something went wrong..."})



