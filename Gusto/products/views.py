from django.shortcuts import render, redirect
from .models import Product, Reviews
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm

# product list view for authorized users
@login_required(login_url="/account/login")
def product_list(request):
    products = Product.objects.all()

    return render(request, 'products/products.html', {'products': products})

# details view of each separate product
@login_required(login_url="/account/login")
def product_details(request, id):
    product = Product.objects.get(id=id)
    user = request.user
    rated = request.POST.get('rating')
    is_wishlist = False # check whether the product is in a user's whishlist, default=False
    new_review = None # set a new review as None first
    
    # set is_wishlist to True if the product is in a user's whishlist
    if product.wishlist.filter(id = request.user.id).exists():
        is_wishlist = True

    # checks whether the user havea lready rated the product. If it has, he cannot rate it again
    if Reviews.objects.filter(user_id = user, product_id = product).exists():
        review_form = ReviewForm()

    # if user has not rated the product yet, then it can leave a review
    else:
        if request.method == 'POST':
            review_form = ReviewForm(data=request.POST)

            # check whether the form is filled correctly
            if review_form.is_valid():
                new_review = review_form.save(commit=False) # save the review, but not in database yet
                new_review.user = user
                new_review.product = product
                new_review.rating = review_form.cleaned_data['rating']
                new_review.save() # now save it into a database
                return redirect('products:product_details', id=product.id)
        else:
            review_form = ReviewForm()

    return render(request, 'products/product_details.html', {'product': product,
    'new_review': new_review, 'review_form': review_form, 'rated': rated, 'is_wishlist': is_wishlist})

# add a product to a wishlist
@login_required(login_url="/account/login")
def wishlist(request, id):
    product = Product.objects.get(id=id)

    # if a product is in a user's wishlist and the user clicks on a heart button,
    # then it removes the product from the whishlist
    if product.wishlist.filter(id = request.user.id).exists():
        product.wishlist.remove(request.user)
    
    # if a product does not exist in a user's whishlist and the user clicks on a heart button,
    # then it adds the product to the whishlist
    else:
        product.wishlist.add(request.user)
    
    return redirect('products:products')