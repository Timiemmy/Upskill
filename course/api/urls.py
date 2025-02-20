from django.urls import include, path
from rest_framework import routers
from . import views

app_name = 'course'

router = routers.DefaultRouter()
router.register('course', views.CourseViewSet)
router.register('subject', views.SubjectViewsets)

urlpatterns = [
    # path('subjects/',views.SubjectListView.as_view(),name='subject_list'),
    # path('subjects/<pk>/',views.SubjectDetailView.as_view(),name='subject_detail'),
    path('', include(router.urls)),
    #path('courses/<pk>/enroll/', views.CourseEnrollView.as_view(),name='course_enroll'),
]