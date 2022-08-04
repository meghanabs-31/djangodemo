from django import views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employeedetail
from .serializers import EmployeeSerializer
# Create your views here.
class Employee(APIView):
    def post(self, request):
        try:
            data = request.data
            user = Employeedetail()
            user.fullname = data["fullname"]
            user.emp_code = data["emp_code"]
            user.mobile = data["mobile"]
            user.skill = data["skill"]
            user.save()
            return Response(ResponseReturn.successfn({"Detail": "Record Added Successfully"}), status = status.HTTP_200_OK)
        except Exception as e:
            return Response(ResponseReturn.failurefn({"Detail": "Issue " + str(e)}), status = status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        try:
            employeedetail = Employeedetail.objects.all()
            serializer = EmployeeSerializer(employeedetail,many=True).data
            return Response(ResponseReturn.successfn(serializer), status = status.HTTP_200_OK)
        except Exception as e:
            return Response(ResponseReturn.failurefn({"status": "Not Found" + str(e)}), status = status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        try:
            data = request.data
            user = Employeedetail.objects.get(id = data["."])
            user.fullname = data["fullname"]
            user.emp_code = data["emp_code"]
            user.mobile = data["mobile"]
            user.skill = data["skill"]
            user.save()
            return Response(ResponseReturn.successfn({"Detail": "Record Updated Successfully"}), status = status.HTTP_200_OK)
        except Exception as e:
            return Response(ResponseReturn.failurefn({"Detail": "Issue " + str(e)}), status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request):
        try:
            data = request.data
            user = Employeedetail.objects.get(fullname = data["fullname"])
            user.delete()
            return Response(ResponseReturn.successfn({"Detail": "Record Deleted Successfully"}), status = status.HTTP_200_OK)
        except Exception as e:
            return Response(ResponseReturn.failurefn({"Detail": "Issue " + str(e)}), status = status.HTTP_500_INTERNAL_SERVER_ERROR)


class get(APIView):
    def get(self,request):
        try:
            data = request.data
            user = Employeedetail.objects.all()
            user.delete()
            return Response(ResponseReturn.successfn({"Detail": "Record Deleted Successfully"}), status = status.HTTP_200_OK)
        except Exception as e:
            return Response(ResponseReturn.failurefn({"Detail": "Issue " + str(e)}), status = status.HTTP_500_INTERNAL_SERVER_ERROR)


class ResponseReturn:
    def successfn(data):
        res = {}
        res["type"] = "Success"
        res["data"] = data
        return res

    def failurefn(data):
        res = {}
        res["type"] = "Fail"
        res["data"] = data
        return res
