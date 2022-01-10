from django.shortcuts import render
from products.models import Product

# search product function
def search_products(request):
    # for logged in user
    if request.user.is_authenticated:
        if request.method == 'POST':
            searched = request.POST.get('search-bar')
            items = Product.objects.filter(title__contains = searched)
            length = len(items)

            if searched == None:
                return render(request, 'searchbar/search_loggedin.html', {'searched': searched})
            else:
                return render(request, 'searchbar/search_loggedin.html', {'searched': searched,
                'items': items, 'length': length})
    
    # for logged out user
    else:
        if request.method == 'POST':
            searched = request.POST.get('search-bar')
            items = Product.objects.filter(title__contains = searched)
            length = len(items)

            if searched == None:
                return render(request, 'searchbar/search.html', {'searched': searched})
            else:
                return render(request, 'searchbar/search.html', {'searched': searched,
                'items': items, 'length': length})

# product details of searched product for users that are not logged in
def search_details(request, id):
    items = Product.objects.get(id=id)

    return render(request, 'searchbar/search_details.html', {'items': items})
