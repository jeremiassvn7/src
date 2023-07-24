import os
from django.apps import apps
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from starlette.middleware.cors import CORSMiddleware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.settings")
apps.populate(settings.INSTALLED_APPS)


def get_application() -> FastAPI:
    fastapi = FastAPI(
                title=settings.APP_NAME,
                version=settings.APP_VERSION,
                docs_url=settings.DOCS_URL,
                openapi_url=settings.OPENAPI_URL,
                debug=settings.DEBUG
            )
    fastapi.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Routers endpoint
    # app.include_router(api_router, prefix="/api")

    # Django
    fastapi.mount("/", WSGIMiddleware(get_wsgi_application()))

    return fastapi


app = get_application()
