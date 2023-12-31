from quart_rate_limiter import (
    QUART_RATE_LIMITER_EXEMPT_ATTRIBUTE,
    QUART_RATE_LIMITER_LIMITS_ATTRIBUTE,
)

from backend.run import app

IGNORED_ENDPOINTS = {"static", "redoc_ui", "openapi", "swagger_ui"}


def rate_limits() -> None:
    for url in app.url_map.iter_rules():
        endpoint = url.endpoint

        exempt = getattr(
            app.view_functions[endpoint],
            QUART_RATE_LIMITER_EXEMPT_ATTRIBUTE,
            False,  # noqa: E501
        )
        if not exempt and endpoint not in IGNORED_ENDPOINTS:
            rate_limits = getattr(
                app.view_functions[endpoint],
                QUART_RATE_LIMITER_LIMITS_ATTRIBUTE,
                [],  # noqa: E501
            )
            assert rate_limits != []
