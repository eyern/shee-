from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from . import views
from django.contrib.auth.models import User
from store.models import Address, Cart, Category, Order, Product
from django.shortcuts import redirect, render, get_object_or_404

class StaticViewSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return ['store:home','store:all-categories']
    
    def location(self, item):
        return reverse(item)