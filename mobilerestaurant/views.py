from django.template import Context, loader
from django.http import HttpResponse
from models import *
from django import forms
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from models import MenuList,Order







def welcome(request, limit=15):
	
	return render_to_response('mobilerestaurant/welcome.html')



@csrf_exempt
def place_order(request, limit=15):
	menu = MenuList.objects.all()
	order = Order.objects.all()
	return render_to_response('mobilerestaurant/order.html', {'menu':menu})  



@csrf_exempt
def placed(request, limit=15):
	newOrder = Order.objects.create(tel_num=request.POST['tel'],block=request.POST['block'],room_num=request.POST['room'])
	for k,v in request.POST.iteritems():
		if k[:4]== 'item' and int(v)>0:
			itemid=int(k[4:])
			mi=MenuList.objects.get(id=itemid)
			newOrderItem = Order.objects.create(order=newOrder, Menulist=mi, quantity=int(v))
	
	print newOrderItem
	return render_to_response('mobilerestaurant/placed.html',{'menu':menu})
	
	
	
def calc_total(request):
	#meal = MenuList.objects.filter(pk==id)
	#order = Order.objects.objects.get(quantity__pk=id)
	order = Order.objects.all()
	print order
	order.order_details = order.Order_item
	
	total_cost = (meal.price*order.quantity) + order.delivery_cost
	return render_to_response('mobilerestaurant/bill.html', {'total_cost':total_cost, 'order':order, 'meal':meal, #'request':request
	})















'''

class OrderForm(ModelForm):
	class Meta:
		model = Order
		exclude=['paid_for', 'total_amount', 'order_details']

@csrf_exempt
def place_order(request, limit=15):
	
	place_order= Order.objects.all()
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			#newOrder = Order.objects.create()
			#newOrder = Order.objects.create(phonenumber=request.POST['tel'],company = comp
			#place_order.order_details = request.POST[form.Order_item]
		return render_to_response('mobilerestaurant/placed.html', {'request':request, 'place_order':place_order})  
	else:
		form = OrderForm()
	
	return render_to_response('mobilerestaurant/order.html', {'form': form.as_p(), 'request':request, 'place_order':place_order})
'''
