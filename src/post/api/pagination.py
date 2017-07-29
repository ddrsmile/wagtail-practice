from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class PostPagePageNumberPagination(PageNumberPagination):
    page_size = 6

    def get_paginated_response(self, data):
        output = {
            'next_page_num': self.page.number + 1 if self.page.number < self.page.paginator.num_pages else None,
            'previous_page_num': self.page.number - 1 if self.page.number > 1 else None,
            'current_page': self.page.number,
            'total_count': self.page.paginator.count,
            'page_range': self.get_page_range(self.page),
            'items': data
        }

        return Response(output)

    def get_page_range(self, page):
        start_index = max(1, page.number - 2)
        end_index = min(start_index + 4, page.paginator.num_pages)

        start_index = min(start_index, max(end_index - 4, 1))

        page_range = [i for i in range(start_index, end_index + 1)]
        return page_range