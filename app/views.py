# from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
# from .models import Company
# from .serializers import CompanySerializer


# class CompanyListAPIView(ListAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer


# class CompanyRetrieveAPIView(RetrieveAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer


# class CompanyCreateAPIView(CreateAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer


# class CompanyUpdateAPIView(UpdateAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer


# class CompanyDestroyAPIView(DestroyAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer


# class CompanyListCreateAPIView(ListCreateAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer


# class CompanyRetrieveUpdateAPIView(RetrieveUpdateAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer


# class CompanyRetrieveDestroyAPIView(RetrieveDestroyAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer


# class CompanyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Company
from .serializers import CompanySerializer


@api_view(['GET'])
def CompanyList(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def CompanyView(request, pk):
    company = Company.objects.get(pk=pk)
    serializer = CompanySerializer(company)
    return Response(serializer.data)


@api_view(['POST'])
def CompanyCreate(request):
    serializer = CompanySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(
        {"message": "Ma'lumotlar noto'g'ri kiritildi!"},
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['PUT', 'PATCH'])
def CompanyUpdate(request, pk):
    company = Company.objects.get(pk=pk)

    serializer = CompanySerializer(company, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(
        {"message": "Kompaniyani yangilashda xatolik yuz berdi!"},
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['DELETE'])
def CompanyDelete(request, pk):
    company = Company.objects.get(pk=pk)
    company.delete()

    return Response(
        {"message": "Kompaniya o'chirildi!"},
        status=status.HTTP_204_NO_CONTENT
    )


@api_view(['GET', 'POST'])
def CompanyListCreate(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CompanySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(
            {"message": "Ma'lumotlar noto'g'ri kiritildi!"},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def CompanyDetail(request, pk):
    company = Company.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CompanySerializer(company, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            {"message": "Kompaniyani to'liq yangilashda xatolik yuz berdi!"},
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == 'PATCH':
        serializer = CompanySerializer(company, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            {"message": "Kompaniyani qisman yangilashda xatolik yuz berdi!"},
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == 'DELETE':
        company.delete()
        return Response(
            {"message": "Kompaniya muvaffaqiyatli o'chirildi!"},
            status=status.HTTP_204_NO_CONTENT
        )
