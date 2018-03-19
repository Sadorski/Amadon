from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    return render(request, 'amadon/index.html')

def buy(request):
    if not 'count' in request.session:
        request.session['count'] = 0
    if not 'price' in request.session:
        request.session['price'] = 0
    if not 'total' in request.session:
        request.session['total'] = 0
    
    if request.method == 'POST':
        print "whats up"
        print request.POST['product_id']
        if int(request.POST['product_id']) == 1015:
            print "hello"
            request.session['price'] = 15.99
        elif int(request.POST['product_id']) == 1016:
            request.session['price'] = 19.99
        elif int(request.POST['product_id']) == 1017:
            request.session['price'] = 25.99
        elif int(request.POST['product_id']) == 1018:
            request.session['price'] = 22.99
            print request.session['price']

        print request.session['price']
        print "hello"
        
        request.session['price'] *= float(request.POST['quantity'])
        request.session['count'] += int(request.POST['quantity'])
        request.session['total'] += float(request.session['price'])
        return redirect('/amadon/thankyou')
    

def thank(request):
    return render(request, 'amadon/thank.html')