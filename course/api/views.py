from rest_framework import generics
from django.db.models import Count
from course.api.serializers import SubjectSerializer
from course.models import Subject


class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.annotate(total_course = Count('courses'))
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.annotate(total_courses=Count('courses'))
    serializer_class = SubjectSerializer


