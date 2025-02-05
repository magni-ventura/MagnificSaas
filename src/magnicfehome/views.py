import pathlib
from django.shortcuts import render
from django.http import HttpResponse
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

# def my_Oldhome_page_view(*args, **kwargs):
#     my_title = "MagnicFE Home"
#     my_context = {
#         "page_title": my_title,
#     }

#     html_ = """
#     <!DOCTYPE html>
#     <html>
#         <head>
#             <title>{{ page_title }}</title>
#         </head>
#         <body>
#             <h1>{{ page_title }}</h1>
#         </body>
#     </html>
#     """.format(page_title=my_title)

#     return HttpResponse(html_)



#     #html_file_path = this_dir / "home.html"
#     #html_ = html_file_path.read_text()
#     return HttpResponse(html_)




def home_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)


def about_view(request, *args, **kwargs):
    queryset = PageVisit.objects.all()
    page_queryset = PageVisit.objects.filter(path = request.path)
    try:
        percent = (page_queryset.count() * 100) / queryset.count()
    except ZeroDivisionError:
        percent = 0

    my_title = "MagnicFE Home"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_queryset.count(),
        "percent" : (page_queryset.count() * 100) / queryset.count(),
        "total_visit_count": queryset.count(),  # added for testing purpose
    }

    path = request.path
    html_template = "home.html"
    PageVisit.objects.create(path = request.path)
    return render(request, html_template, my_context)