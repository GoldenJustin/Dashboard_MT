from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from .serializers import *


def dash_board(request):
    reporter = Reporter.objects.all()
    scammer = Scammer.objects.all()
    total_reports = reporter.count()
    ripoti = Info.objects.all()
    context = {
        'reporter': reporter,
        'scammer': scammer,
        'ripoti': ripoti,
        'total_reports': total_reports
    }
    return render(request, 'dashboard/dash_board.html', context)


def general_reports(request):
    return render(request, 'dashboard/general_reports.html')


def reports(request):
    ripoti = Info.objects.all()
    context = {
        'ripoti': ripoti
    }
    return render(request, 'dashboard/reports.html', context)


# API function Begin.................

def info_fun(request):
    info = Info.objects.all()
    serializer = InfoSerializer(info, many=True)
    return JsonResponse({'info': serializer.data})

# def reporter_fun(request):
#     reporter = Reporter.objects.all()
#     serializer = ReporterSerializer(reporter, many=True)
#     return JsonResponse({'reporter': serializer.data})
#
#
# def scammer_fun(request):
#     scammer = Scammer.objects.all()
#     serializer = ScammerSerializer(scammer, many=True)
#     return JsonResponse({'scammer': serializer.data})
