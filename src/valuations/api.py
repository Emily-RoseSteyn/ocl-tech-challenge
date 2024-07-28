from datetime import datetime
from typing import List

from django.core.paginator import Paginator
from ninja import NinjaAPI, Schema

from valuations.constants import CITY_CHOICES, ROLL_TYPE_CHOICES
from valuations.models import Valuation

api = NinjaAPI()


class ValuationSchema(Schema):
    last_modified: datetime
    city: str = CITY_CHOICES["durban"]
    roll_type: str = ROLL_TYPE_CHOICES["full_title"]
    rate_number: str = '05100037'
    legal_description: str = 'Portion 16 of ERF 74 of AMANZIMTOTI'
    address: str = '26 SOMERSET WAY, AMANZIMTOTI'
    first_owner: str = 'CRUCHINHO RUI PEREIRA'
    use_code: str = 'Single Residential (15)'
    rating_category: str = 'Residential'
    market_value: float = 1830000.000
    registered_extent: float = 1634.000


class PaginationDetails(Schema):
    page: int = 1
    per_page: int = 10  # TODO: Could come from config
    total_pages: int = 100
    count: int = 1000


class PaginatedResponseSchema(Schema):
    """
    This is the paginated response schema.
    """
    data: List[ValuationSchema]
    pagination: PaginationDetails


@api.get("", response=PaginatedResponseSchema)
def get(request, page: int = 1):
    # TODO: Could generalise this pagination and add filtering/searching
    valuations_list = Valuation.objects.all().order_by('rate_number').values()
    # Show 10 valuations per page
    number_per_page = 10  # TODO: Could come from config
    paginator = Paginator(valuations_list, number_per_page)

    current_page_number = page

    # TODO: Clean up these checks - don't like that it's nested
    if current_page_number and current_page_number < 1:
        current_page_number = 1
    elif current_page_number and current_page_number > paginator.num_pages:
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
