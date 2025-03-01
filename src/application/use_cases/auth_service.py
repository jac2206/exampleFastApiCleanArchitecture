class AuthService:
    def get_roles(self, user_id: int):
        return ["admin", "editor"]
