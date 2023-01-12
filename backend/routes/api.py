# Import from application modules
from routes.Login import LoginApi
from routes.User import AdminApi
# from routes.User import AdminApi, UserApi


# Function to initialize route to API Flask
def initialize_routes(api):
    api.add_resource(AdminApi, '/api/create_user')
    api.add_resource(LoginApi, '/api/get_token')
