from django.shortcuts import render
def power(request):
    context=()
    context['POWER'] ="0"
    context['I'] = "0"
    context['R'] = "0"
    if request.method == 'POST':
        print("POST method is used")
        I=request.POST.get('instensity', '0')
        R=request.POST.get('resistance', '0')
        print('request', request)
        print('INTENSITY=', I)
        print('RESISTANCE=',R)
        POWER= int(I)**2*int(R)
        context['[POWER]'] = POWER
        context['I']=I
        context['R']=R
        print('POWER', POWER)
    return render (request, 'mathapp/power.html',context)