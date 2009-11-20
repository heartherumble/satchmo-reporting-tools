from django.contrib.admin.views.decorators import staff_member_required
from reporting_tools.filter import OrderFilterSet

@staff_member_required
def sales_report(request, template='admin/reports/sales_report.html'):
	f = OrderFilterSet(request.GET, queryset=Order.objects.all())
	sales_total = f.qs.aggregate(order_total=Sum('total'))
	ctx = {'f': f, 'sales_total': sales_total }
	return render_to_response(template, RequestContext(request, ctx))