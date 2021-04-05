from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin

# 继承哪个视图类合适
from emp.models import Employee
from emp.serializer import EmployeeModelSerializer


class EmployeeAPIView(ListModelMixin, GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
