from django.contrib.sitemaps import Sitemap

from .models import Product


class ProductSitemap(Sitemap):

    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return (Product.objects.filter
                (archived__isnull=False)
                .order_by('-created_at')
                )

    def lastmod(self, obj):
        return obj.created_at