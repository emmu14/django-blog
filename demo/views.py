from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.http import JsonResponse
from articles.models import article


TMDB_API_KEY ='ca226725f5aa54d5b10ab63f4c06ebba'



def homepage(request):
    return render(request,"")
def aboutpage(request):
    return render(request,"about.html")

def movie(request):
    movies = []
    query = request.GET.get("q")
    error = None

    if query:
        try:
            response = requests.get(
                "https://api.themoviedb.org/3/search/movie",
                params={
                    "api_key": TMDB_API_KEY,
                    "query": query
                },
                timeout=10
            )

            print("STATUS:", response.status_code)
            print("RESPONSE:", response.text[:500])

            response.raise_for_status()

            movies = response.json().get("results", [])

        except requests.exceptions.RequestException as e:
            print("ERROR:", e)
            error = str(e)

    return render(
        request,
        "movies.html",
        {
            "movies": movies,
            "query": query,
            "error": error
        }
    )





def articleapi(request):
    articles = list(
        article.objects.values(
            "title",
            "slug",
            "body",
            "date",
            "thumb",
            "author",
            "price",
        )
    )

    return JsonResponse(articles, safe=False)