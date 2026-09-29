import hashlib
import os
from getpass import getpass
from cinema import storage
from cinema.log_setup import get_logger

log = get_logger()


def hash_password(password, salt):
    return hashlib.sha256((salt + password).encode()).hexdigest()


def create_admin(user_id, password):
    salt = os.urandom(8).hex()
    storage.save("admin.json", {
        "id": user_id,
        "salt": salt,
        "hash": hash_password(password, salt),
    })


def check_login(user_id, password):
    admin = storage.load("admin.json", None)
    if admin is None:
        return False
    return (user_id == admin["id"] and
            hash_password(password, admin["salt"]) == admin["hash"])


def first_time_setup():
    if storage.load("admin.json", None) is None:
        print("First run - create the admin account")
        uid = input("Choose admin ID: ")
        pwd = getpass("Choose password: ")
        create_admin(uid, pwd)
        log.info("Admin account created")


def login():
    print("=====Log In=====")
    uid = input("Enter User ID: ")
    pwd = getpass("Enter password: ")
    if check_login(uid, pwd):
        log.info("Admin login: %s", uid)
        return True
    log.warning("Failed login attempt for %s", uid)
    return False
