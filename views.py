
from .forms import  PageUploadForm
from django.shortcuts import render , get_object_or_404

def upload(request):
    if request.method == 'POST':
        page_upload_form=PageUploadForm(data=request.POST,files=request.FILES)

        if page_upload_form.is_valid():
            page_upload_form.save()
    else:
        page_upload_form=PageUploadForm()

    return render(request,'upload.html',{'page_upload_form':page_upload_form})
