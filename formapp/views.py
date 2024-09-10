from django.shortcuts import render

# Create your views here.
def simple_form(request):
    return render(request, 'formapp/simple_form.html')



def payment_form(request):
    if request.method == 'GET':
        return render(request, 'formapp/payment_form.html')
    else:
        print('expecting to post data')
        return render(request, 'formapp/simple_form.html')