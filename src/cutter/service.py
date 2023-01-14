import random
import string
from django.utils import timezone

from cutter.models import Urls


def make_shorten(url):
    random_hash = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(7))
    mapping = Urls(original_url=url, hash=random_hash, created_at=timezone.now())
    mapping.save()
    return random_hash


def load_url(url_hash):
    return Urls.objects.get(hash=url_hash)
