from django.shortcuts import render
from item.models import Item, ItemLink

def index(request):
	items1 = Item.objects.filter(main1=True)
	items2 = Item.objects.filter(main2=True)
	context = {'items1':items1,'items2':items2}
	return render(request,'item/index.html', context)

def search(request):
	q = request.GET.get('q')
	items = Item.objects.filter(title__contains = q)
	test = Item.objects.get(pk=1)
	value = test.get_max_price
	context={'q':q,'items':items,'test':value}
	return render(request,'item/search.html', context)

def detail(request):
	it_id = request.GET.get('id')
	item = Item.objects.get(pk = it_id)
	links = ItemLink.objects.filter(item=item)
	context = {'item':item,'links':links}
	return render(request,'item/detail.html', context)
