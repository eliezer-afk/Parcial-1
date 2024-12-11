from app.home import home_bp, home_resource
from app.user import user_bp, user_resource
from app.auth import auth_bp, auth_resource

class RouteApp:
    def init_app(self, app, docs):
        self.register_blueprints(app)
        self.register_docs(docs)

    def register_blueprints(self, app):
        app.register_blueprint(home_bp, url_prefix='/api/v1')
        app.register_blueprint(user_bp, url_prefix='/api/v1')
        app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')

    def register_docs(self, docs):
        docs.register(home_resource.index, blueprint='home')
        docs.register(user_resource.index, blueprint='user')
        docs.register(user_resource.find, blueprint='user')
        docs.register(user_resource.find_by_email, blueprint='user')
        docs.register(user_resource.post_user, blueprint='user')
        docs.register(user_resource.update_user, blueprint='user')
        docs.register(user_resource.delete_user, blueprint='user')
        docs.register(user_resource.find_by_username, blueprint='user')
        docs.register(auth_resource.login, blueprint='auth')
        docs.register(auth_resource.register, blueprint='auth')
