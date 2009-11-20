from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Avg, Sum
from django.shortcuts import render_to_response
from django.template import RequestContext

from product.models import Product

from reporting_tools.filters import OrderFilterSet

from satchmo_store.shop.models import Order, OrderItem

@staff_member_required
def orders_report(request, template='admin/reports/orders_report.html'):
	f = OrderFilterSet(request.GET, queryset=Order.objects.all())
	sales_total = f.qs.aggregate(order_total=Sum('total'))
	ctx = {'f':f, 'sales_total':sales_total }
	return render_to_response(template, RequestContext(request, ctx))
	
@staff_member_required
def products_report(request, template='admin/reports/products_report.html'):
    products = Product.objects.filter(total_sold__gt=0).order_by('-total_sold').annotate(average_price=Avg('orderitem__unit_price'), total_sales=Sum('orderitem__line_item_price'))[:10]
    ctx = {'products':products}
    return render_to_response(template, RequestContext(request, ctx))