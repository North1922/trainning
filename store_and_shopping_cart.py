# 7) Магазин и корзина
#
# Классы: Product (база), Food, Clothes, Cart.
# Методы: Cart.add(product, qty), remove(product, qty), total().
# Проверки: qty > 0; склад (опционально) не уходит в минус.
# Усложнение (паттерны): PricingStrategy (купоны, скидки по категории); налоги как отдельная стратегия.

# 7) Магазин и корзина
#
# Сущности: Product (база), Food, Clothes, Inventory, Cart, Coupon, TaxPolicy.
#
# Атрибуты:
#
# Product: sku, name, base_price.
#
# Food: expiry_date.
#
# Clothes: size, color.
#
# Inventory: карта sku → available_qty.
#
# Cart: позиции sku → qty, применённые купоны.
#
# Методы (обязательные):
#
# Inventory.add(sku, qty) / remove(sku, qty) — контроль неотрицательности.
#
# Cart.add(product, qty) / remove(product, qty) — qty > 0.
#
# Cart.total(tax_policy, coupons) — сумма: базовая цена × qty + налоги − скидки.
#
# TaxPolicy.compute(product, subtotal) — стратегия.
#
# Coupon.apply(cart) — стратегия скидки (по SKU/категории/сумме).
#
# Проверки/ошибки: превышение доступного склада (если контролируешь на этапе добавления); купон несовместим/просрочен.
#
# Инварианты: количество в корзине ≥ 0.
#
# Усложнения: резервы склада при добавлении; пересчёт при смене количества; стек стратегии налогообложения.