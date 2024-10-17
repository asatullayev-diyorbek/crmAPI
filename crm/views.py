from rest_framework import status, authentication
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, Course, Enrollment, Lesson, Assignment
from .serializers import UserSerializer, CourseSerializer, EnrollmentSerializer, LessonSerializer, AssignmentSerializer
from .permissions import IsAuth, IsAuthToken


# Token authorization ishlatilgan
class UserListView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthToken]
    def get(self, request):
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = UserSerializer(data=request.data)
        if data.is_valid():
            try:
                user = data.create(data.validated_data)
                context = {
                    'message': "Foydalanuvchi yaratildi",
                    'user': UserSerializer(user).data
                }
                return Response(context, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


# Token authorization ishlatilgan
class UserDetailView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthToken]
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'message': 'Foydalanuvchi topilmadi'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            updated_user = serializer.save()
            context = {
                'message': "Foydalanuvchi ma'lumotlari yangilandi",
                'user': UserSerializer(updated_user).data
            }
            return Response(context, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            User.objects.get(pk=pk).delete()
            return Response({'message': "O'chirildi"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'message': 'Foydalanuvchi topilmadi'}, status=status.HTTP_404_NOT_FOUND)


# Token authorization ishlatilgan
class CourseListView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthToken]

    def get(self, request):
        courses = Course.objects.all()
        courses_serializer = CourseSerializer(courses, many=True)
        return Response(courses_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = CourseSerializer(data=request.data)
        if data.is_valid():
            try:
                course = data.create(data.validated_data)
                context = {
                    'message': "Kurs yaratildi",
                    'course': CourseSerializer(course).data
                }
                return Response(context, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

# Token authorization ishlatilgan
class CourseDetailView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthToken]

    def get(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
            course_serializer = CourseSerializer(course)
            return Response(course_serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response({'message': 'Kurs topilmadi'}, status=status.HTTP_404_NOT_FOUND)
        #
        # # `teacher_id` ni olish uchun request.data ni to'ldiramiz
        # request_data = request.data.copy()  # To'liq copy qilish
        # if 'teacher_id' in request_data:
        #     request_data['teacher'] = {'id': request_data.pop('teacher_id')}  # Teacher_id ni to'g'ri formatda ko'rsatamiz
        print(request.data)
        serializer = CourseSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            updated_course = serializer.update(course, serializer.validated_data)  # `save` metodidan foydalanamiz, chunki `update` qo'shimcha xatolar keltirib chiqarishi mumkin
            context = {
                'message': "Kurs ma'lumotlari yangilandi",
                'course': CourseSerializer(updated_course).data
            }
            return Response(context, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            Course.objects.get(pk=pk).delete()
            return Response({'message': "O'chirildi"}, status=status.HTTP_200_OK)
        except Course.DoesNotExist:
            return Response({'message': 'Kurs topilmadi'}, status=status.HTTP_404_NOT_FOUND)

class EnrollmentListView(APIView):
    permission_classes = [IsAuth]

    def get(self, request):
        enrollments = Enrollment.objects.all()
        serializer = EnrollmentSerializer(enrollments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            enrollment = serializer.create(serializer.validated_data)
            context = {
                'message': "Ro'yxatdan o'tish yaratildi",
                'enrollment': EnrollmentSerializer(enrollment).data
            }
            return Response(context, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EnrollmentDetailView(APIView):
    permission_classes = [IsAuth]

    def get(self, request, pk):
        try:
            enrollment = Enrollment.objects.get(pk=pk)
            serializer = EnrollmentSerializer(enrollment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Enrollment.DoesNotExist:
            return Response({'message': 'Ro\'yxatdan o\'tish topilmadi'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            enrollment = Enrollment.objects.get(pk=pk)
        except Enrollment.DoesNotExist:
            return Response({'message': 'Ro\'yxatdan o\'tish topilmadi'}, status=status.HTTP_404_NOT_FOUND)

        serializer = EnrollmentSerializer(enrollment, data=request.data, partial=True)
        if serializer.is_valid():
            updated_enrollment = serializer.update(enrollment, serializer.validated_data)
            context = {
                'message': "Ro'yxatdan o'tish ma'lumotlari yangilandi",
                'enrollment': EnrollmentSerializer(updated_enrollment).data
            }
            return Response(context, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            enrollment = Enrollment.objects.get(pk=pk)
            enrollment.delete()
            return Response({'message': "O'chirildi"}, status=status.HTTP_200_OK)
        except Enrollment.DoesNotExist:
            return Response({'message': 'Ro\'yxatdan o\'tish topilmadi'}, status=status.HTTP_404_NOT_FOUND)


class LessonListView(APIView):
    permission_classes = [IsAuth]

    def get(self, request):
        lessons = Lesson.objects.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LessonSerializer(data=request.data)
        if serializer.is_valid():
            lesson = serializer.create(serializer.validated_data)
            context = {
                'message': "Dars muvaffaqiyatli yaratildi",
                'lesson': LessonSerializer(lesson).data
            }
            return Response(context, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LessonDetailView(APIView):
    permission_classes = [IsAuth]

    def get(self, request, pk):
        try:
            lesson = Lesson.objects.get(pk=pk)
            serializer = LessonSerializer(lesson)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Lesson.DoesNotExist:
            return Response({'message': 'Dars topilmadi'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            lesson = Lesson.objects.get(pk=pk)
        except Lesson.DoesNotExist:
            return Response({'message': 'Dars topilmadi'}, status=status.HTTP_404_NOT_FOUND)

        serializer = LessonSerializer(lesson, data=request.data, partial=True)
        if serializer.is_valid():
            updated_lesson = serializer.update(lesson, serializer.validated_data)
            context = {
                'message': "Dars ma'lumotlari yangilandi",
                'lesson': LessonSerializer(updated_lesson).data
            }
            return Response(context, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            Lesson.objects.get(pk=pk).delete()
            return Response({'message': "O'chirildi"}, status=status.HTTP_200_OK)
        except Lesson.DoesNotExist:
            return Response({'message': 'Dars topilmadi'}, status=status.HTTP_404_NOT_FOUND)


class AssignmentListView(APIView):
    permission_classes = [IsAuth]

    def get(self, request):
        assignments = Assignment.objects.all()
        serializer = AssignmentSerializer(assignments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            assignment = serializer.create(serializer.validated_data)
            context = {
                'message': "Vazifa muvaffaqiyatli yaratildi",
                'assignment': AssignmentSerializer(assignment).data
            }
            return Response(context, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssignmentDetailView(APIView):
    permission_classes = [IsAuth]

    def get(self, request, pk):
        try:
            assignment = Assignment.objects.get(pk=pk)
            serializer = AssignmentSerializer(assignment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Assignment.DoesNotExist:
            return Response({'message': 'Vazifa topilmadi'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            assignment = Assignment.objects.get(pk=pk)
        except Assignment.DoesNotExist:
            return Response({'message': 'Vazifa topilmadi'}, status=status.HTTP_404_NOT_FOUND)

        serializer = AssignmentSerializer(assignment, data=request.data, partial=True)
        if serializer.is_valid():
            updated_assignment = serializer.update(assignment, serializer.validated_data)
            context = {
                'message': "Vazifa ma'lumotlari yangilandi",
                'assignment': AssignmentSerializer(updated_assignment).data
            }
            return Response(context, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            Assignment.objects.get(pk=pk).delete()
            return Response({'message': "O'chirildi"}, status=status.HTTP_200_OK)
        except Assignment.DoesNotExist:
            return Response({'message': 'Vazifa topilmadi'}, status=status.HTTP_404_NOT_FOUND)

