from django.shortcuts import render,redirect

from dataentery.utils import get_all_custom_model
from upload.models import Uploads

from django.core.management import call_command

 
# Create your views here.
def import_data(request):
    context=None
    if request.method=='POST':
        file_path=request.FILES.get('file_path')
        model_name=request.POST.get('model_name')
        upload=Uploads.objects.create(file=file_path,model_name=model_name)
        try:
            call_command('importdata',upload.full_path(),model_name)
        except Exception as e:
            raise e
        return redirect('import_data')
    else:
        all_models=get_all_custom_model()
        context={'all_models':all_models}
    return render(request,'dataentery/importdata.html',context)
    