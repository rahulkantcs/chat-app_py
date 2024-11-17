from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://chatapp:root@localhost/"
DATA_BASE = "chatapp"
async def startup_db_client(app):
    app.mongodb_client = AsyncIOMotorClient(MONGO_URI)
    app.mongodb = app.mongodb_client.get_database(DATA_BASE)
    print("MongoDB connected.")

# method to close the database connection
async def shutdown_db_client(app):
    app.mongodb_client.close()
    print("Database disconnected.")

async def lifespan(app):
    # Start the database connection
    await startup_db_client(app)
    yield
    # Close the database connection
    await  shutdown_db_client(app)
