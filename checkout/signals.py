import django.dispatch


checkout_attempt = django.dispatch.Signal(
    providing_args=["order", "result"]
)

post_create_customer = django.dispatch.Signal(
    providing_args=["user", "success", "reference_id", "error", "results"]
)

confirm_attempt = django.dispatch.Signal(
    providing_args=["order", "transaction"]
)

charge = django.dispatch.Signal(
    providing_args=["order", "transaction", "success", "data"]
)

subscribe = django.dispatch.Signal(
    providing_args=["order", "transaction", "success", "data", "request"]
)

order_complete = django.dispatch.Signal(
    providing_args=["order", ]
)
