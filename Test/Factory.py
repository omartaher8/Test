import factory
from service.models import Product

class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n)
    name = factory.Faker("word")
    category = factory.Faker("word")
    available = factory.Faker("boolean")
    price = factory.Faker("pyfloat", left_digits=2, right_digits=2, positive=True)
