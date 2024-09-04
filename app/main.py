from fastapi import FastAPI
from starlette.responses import RedirectResponse

#Routers
from routes.user import users_route
from routes.animal import animals_route
from routes.vehicle import vehicles_route
from routes.product import products_route
from routes.venta import ventas_route


app = FastAPI()

#On Startup
#On Shutdown

#Documentation
@app.get("/")
async def docs():
    return RedirectResponse(url="/docs")

#localhost:9090/
#Rutas
app.include_router(users_route, prefix="/users", tags=["Users"])
app.include_router(animals_route, prefix="/animals", tags=["Animals"])
app.include_router(vehicles_route, prefix="/vehicles", tags=["Vehicles"])
app.include_router(products_route, prefix="/products", tags=["Products"])
app.include_router(ventas_route, prefix="/ventas", tags=["Ventas"])