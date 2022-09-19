import datetime
from io import BytesIO

from django.utils import timezone
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa  

def get_time_now():
    datee =datetime.datetime.strptime(str(timezone.now()), "%Y-%m-%d %H:%M:%S.%f")
    year = datee.year
    month = datee.month
    day = datee.day
    return [year, month, day]

def html_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    # print(html)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None