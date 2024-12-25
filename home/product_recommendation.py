from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .models import Product

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .models import Product

def get_similar_product(product_id, top_n = 10):
    vectorize = TfidfVectorizer(stop_words = "english")
    product_description = Product.objects.all().values_list('description', flat = True)
    tfid_matrix = vectorize.fit_transform(product_description)
    target_product = Product.objects.get(id = product_id)
    all_product = list(Product.objects.all())
    target_index = all_product.index(target_product)
    cosine_sim = cosine_similarity(tfid_matrix[target_index], tfid_matrix).flatten()
    similar_indices = cosine_sim.argsort()[-top_n-1:-1][::-1]
    similar_indices = [i for i in similar_indices if i != target_index]
    similar_products = []
    for idx in similar_indices:
        similar_products.append(all_product[idx])
    return similar_products