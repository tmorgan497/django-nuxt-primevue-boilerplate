# backend/backend/api.py

from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController


api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)


@api.get("/")
def index(request):
    return {"message": "Main API"}


@api.get("status/")
def status(request):
    return {"status": "ok"}
