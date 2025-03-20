from http.client import responses
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from spacy.lang.sv.tokenizer_exceptions import capitalized
from thinc.layers.padded2list import forward
from django.urls import reverse
from django.template.loader import render_to_string


monthly_challenges = {
    "january":"January is month of India's Republic Day!",
    "february":"February is Valentine Month.",
    "march":"March is where Indian celebrate holi.",
    "april":"April is a month of fools.",
    "may":"May is a month of peak summer.",
    "june":"June is the start of the Monsoon.",
    "july":"July is the peak monsoon.",
    "august":"August is india independance day.",
    "september":"september1",
    "october":"october1",
    "november":"november1",
    "december":None

}

# Create your views here.
# def january(request):
#
#     return HttpResponse("Eat atleast 6 meals every day in January.")
#
# def february(request):
#     return HttpResponse("Walk for at atleast 20 minutes every day in February.")
#
# def march(request):
#     return HttpResponse("Learn Django for atleast 20 minutes every day in march.")


def index(request):
    list_items  =  ""
    months = list(monthly_challenges.keys())
    # for month in months:
    #     capitalized_month  = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href = \"{month_path}\">{capitalized_month}</a></li>"
    #
    # respone_data = f"<ul>{list_items}</ul>"

    return render(request, "challenges/index.html",{
        "months":months
    })
    return HttpResponse(respone_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # this will look like /challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        #response_data = f"<h1>{challenge_text}</h1>"

        #response_data = render_to_string(("challenges/challenge.html"))
        #return HttpResponse(response_data)
        return render(request, "challenges/challenge.html",{
            "text":challenge_text,"month_name":month.capitalize()
        })
    except:
        return  HttpResponseNotFound("<h1>This month is not supported</h1>")
    # if month == 'january':
    #     challenge_text = "Eat atleast 6 meals every day in January."
    # elif month =='february':
    #     challenge_text = "Walk for at atleast 20 minutes every day in February."
    # elif month == "march":
    #     challenge_text = "Learn Django for atleast 20 minutes every day in march."
    # else:
    #     return HttpResponseNotFound("This month is not Supported")


