from django.urls import path

from . import views


app_name = 'crm'
urlpatterns = [
    path('user/list/', views.UserListView.as_view(), name="user-list"),
    path('user/<int:pk>/detail/', views.UserDetailView.as_view(), name="user-detail"),

    path('course/list/', views.CourseListView.as_view(), name="course-list"),
    path('course/<int:pk>/detail/', views.CourseDetailView.as_view(), name="course-detail"),

    path('enrollment/list/', views.EnrollmentListView.as_view(), name="enrollment-list"),
    path('enrollment/<int:pk>/detail/', views.EnrollmentDetailView.as_view(), name="enrollment-detail"),

    path('lesson/list/', views.LessonListView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/detail/', views.LessonDetailView.as_view(), name='lesson-detail'),

    path('assignment/list/', views.AssignmentListView.as_view(), name='assignment-list'),
    path('assignment/<int:pk>/detail/', views.AssignmentDetailView.as_view(), name='assignment-detail'),
]