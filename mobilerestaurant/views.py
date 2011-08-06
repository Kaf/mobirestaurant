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
	return render_to_response('mobilerestaurant/order.html', {'menu':menu,'order':order})  



@csrf_exempt
def bill(request, limit=15):
	total = 0
	food = ' '
	newOrder = Order.objects.create(tel_num=request.POST['tel'],block=request.POST['block'],room_num=request.POST['room'])
	for k,v in request.POST.iteritems():
		if k[:4]== 'item' and int(v)>0:
			itemid=int(k[4:])
			mi=MenuList.objects.get(id=itemid)
			newOrderItem = OrderItem.objects.create(order=newOrder, menuitem=mi, quantity=int(v))
			total += int(v)*mi.price
			food += "Item:"+  str(MenuList.objects.get(id=itemid).menu_item)+"   " +"quantity:  " + str(newOrderItem.quantity) +"\n"
	#print mi
	#print newOrderItem
	newOrder.total_amount = total 
	newOrder.order_details = food
	indfood = newOrder.order_details.split('\n')[:-1]
	newOrder.save()
	return render_to_response('mobilerestaurant/bill.html', {'total':total,'indfood':indfood})
	
	
	
def placed(request):
	return render_to_response('mobilerestaurant/placed.html')















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
