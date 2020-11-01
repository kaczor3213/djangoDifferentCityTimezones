from django.shortcuts import render
from django.views.generic import View
from django.http import Http404
from datetime import datetime
import pytz
# Create your views here.

class ThreeCitiesTimezone(View):
    def get(self, request):
        now = datetime.now()
        utc = pytz.utc
        
        new_york_tz = pytz.timezone('America/New_York')
        lublin_tz = pytz.timezone('Europe/Warsaw')
        sydney_tz = pytz.timezone('Australia/Sydney')
        fmt = '%Y,%m,%d,%H,%M,%S'

        lublin_dt = lublin_tz.localize(now)
        lublin_str = lublin_dt.strftime(fmt)
        new_york_dt = lublin_dt.astimezone(new_york_tz)
        new_york_str = new_york_dt.strftime(fmt)
        sydney_dt = lublin_dt.astimezone(sydney_tz)
        sydney_str = sydney_dt.strftime(fmt)

        times = {
            "new_york": new_york_str,
            "lublin": lublin_str,
            "sydney": sydney_str,
        }
        return render(request, 'index/index.html', times)

    def post(self, request):
        raise Http404("coś się zjebało")
