class User:
    def create_user(self, username, password, email):
        print("registered user in db")

    def send_email(self, subject, to_email):
        print("email sent")

    def log_error(self, error):
        print("log:", error)

    def register_user(self, username, password, email):
            self.create_user(username, password, email)
            self.send_email("user registered", email)


if __name__ == '__main__':
    user = User()
    user.register_user("anji", "secret", "anji@example.com")
