from django.shortcuts import render
from test_app.models import AccessRecord

# Create your views here.
def index(request):
    webpages = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages}
    return render(request=request, template_name='test_app/index.html', context=date_dict)