from rest_framework.serializers import ModelSerializer

from emp.models import Employee


class EmployeeModelSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id","emp_name", "salary", "age", "photo"]
