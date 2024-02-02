class UserDB:
    def create_user(self, username, password, email):
        print("registered user in db")


class Email:
    def send_email(self, subject, to_email):
        print("email sent")


class User:
    def register_user(self, username, password, email):
        user_db = UserDB()
        user_db.create_user(username, password, email)
        email_server = Email()
        email_server.send_email("user registered", email)


if __name__ == '__main__':
    user = User()
    user.register_user("anji", "secret", "anji@example.com")
