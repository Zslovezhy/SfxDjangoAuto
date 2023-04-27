from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import UploadLog

# Create your views here.
def uploadLog(request):
    if request.method == "POST":
        upload = UploadLog()
        bugID = request.POST.get("bugID")
        caseName = request.POST.get("caseName")
        FwVersion = request.POST.get("FwVersion")
        IP = request.POST.get("IP")
        nodeName = request.POST.get("nodeName")
        configID = request.POST.get("configID")
        upload.bugID = bugID
        upload.caseName = caseName
        upload.FwVersion = FwVersion
        upload.IP = IP
        upload.nodeName = nodeName
        upload.configID = configID
        upload.save()
        return HttpResponse("上传成功！")
    else:
        return render(request, 'UploadLog.html')