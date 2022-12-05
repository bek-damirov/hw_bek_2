from shop.models import Item, Purchase


s = Item.objects.create(name='TV', price='40000')


s.purchase_set.create(name='Azamat', age='26', data_purchase='2010,01,09')
s.purchase_set.create(name='Baha', age='28', data_purchase='2010,07,09')

s.purchase_all()

