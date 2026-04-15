from discount_service import DiscountService
from discount_strategy import DiscountStrategy
from diwali import DiwaliDiscount
from holi import HoliDiscount

diwali_str = DiwaliDiscount()
holi_str = HoliDiscount()

discount_svc = DiscountService(diwali_str)
discount_svc.process()

discount_svc.set_strategy(holi_str)
discount_svc.process()



