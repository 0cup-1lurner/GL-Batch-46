class Account:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    @property
    def password(self):
        raise AttributeError("Password is write only")
    
    @password.setter
    def password(self, password):
        # Hash here
        self._password = password

        
