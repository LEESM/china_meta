from django.db import models

class Item(models.Model):
	brand = models.CharField(max_length=50, default='')
	title = models.CharField(max_length=100, default='')
	image = models.ImageField(blank=True, upload_to='')
	pub_date = models.DateTimeField(auto_now_add=True)
	detail = models.TextField(blank=True)
	main1 = models.BooleanField(default=False)
	main2 = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	def get_min_price(self):
		links = ItemLink.objects.filter(item=self)
		min_price = 999999999
		for link in links:
			if(min_price > link.price):
				min_price = link.price
		return min_price

	def get_max_price(self):
		links = ItemLink.objects.filter(item=self)
		max_price = 0
		for link in links:
			if(max_price < link.price):
				max_price = link.price
		return max_price


class ItemLink(models.Model):
	item = models.ForeignKey(Item,blank=True, null=True)
	source_name = models.CharField(max_length=100)
	source_url = models.CharField(max_length=256)
	price = models.FloatField(default=0)
	delivery = models.CharField(max_length=100)
	additional_benefit = models.CharField(max_length=100)
	def __str__(self):
		return self.source_name

