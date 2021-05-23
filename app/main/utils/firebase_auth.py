from firebase_admin import auth, credentials
import firebase_admin

def user_setter(email, password, name):
    user = auth.create_user(
        email=email,
        password=password,
        display_name = name,
        email_verified=False,
        disabled=False
    )
    return user

def user_getter(uid):
    result = auth.get_user(uid)
    return result
