from django.core.paginator import Paginator
from ninja import NinjaAPI

from valuations.models import Valuation

api = NinjaAPI()


@api.get("")
def get(request):
    # TODO: Could generalise this pagination and add filtering/searching
    valuations_list = Valuation.objects.all().order_by('rate_number').values()
    # Show 10 valuations per page
    number_per_page = 10
    paginator = Paginator(valuations_list, number_per_page)

    current_page_number = request.GET.get("page")

    # TODO: Clean up these checks - don't like that it's nested
    if current_page_number and current_page_number.isdigit():
        current_page_number = int(request.GET.get("page"))

        if current_page_number < 1:
            current_page_number = 1
        elif current_page_number > paginator.num_pages:
            current_page_number = paginator.num_pages
    else:
        current_page_number = 1

    page_obj = paginator.get_page(current_page_number)
    data = list(page_obj.object_list)

    return {
        "data": data,
        "pagination": {
            "page": current_page_number,
            "per_page": number_per_page,
            "total_pages": paginator.num_pages,
            "count": paginator.count
        }
    }