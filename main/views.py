from .models import Employee, Events, Challenge, Team
from .serializers import EmployeeSerializer, EventsSerializer, \
    ChallengeSerializer, RatingEmployeeSerializer, RatingTeamSerializer
from rest_framework.views import APIView
from django.http import Http404, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# да, знаю что за такое надо руки отрывать, но хакатон близился к концу, а фича только придумалась
y = [0 for i in range(10)]

class EmployeeView(APIView):

    def get_object(self,  pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        # print(request.headers.get('User-Agent'))
        return Response(serializer.data)


class EventsView(APIView):

    def get(self, request):
        events = Events.objects.all()
        serializer = EventsSerializer(events, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def challenge(request, r_type):
    if request.method == 'GET':
        if r_type == 'daily':
            challenges = Challenge.objects.all().filter(ch_type='дневные')
        elif r_type == 'sprint':
            challenges = Challenge.objects.all().filter(ch_type='на спринт')
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ChallengeSerializer(challenges, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def rating(request, r_type):
    if request.method == 'GET':
        if r_type == 'employee':
            serializer = RatingEmployeeSerializer(Employee.objects.all().order_by('rating'), many=True)
        elif r_type == 'team':
            serializer = RatingTeamSerializer(Team.objects.all().order_by('rating'), many=True)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)


@api_view(['GET'])
def poll(request, option):
    if request.method == 'GET' and 0<option<11:
        y[option-1] += 1
    return HttpResponse('')


@api_view(['GET'])
def show_poll(request):
    import matplotlib.pyplot as plt
    n=len(y)
    x=range(n)
    plt.bar(range(n), y, 1, color='blue')
    plt.savefig('assessment.png')
    image_data = open("assessment.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")
