# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "your_auth_token"
client = Client(account_sid, auth_token)

map_permissions = client.preview \
                        .sync \
                        .services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                        .sync_maps("MPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                        .sync_map_permissions \
                        .list()

for map_permission in map_permissions:
    print(map_permission.unique_name)
    print(map_permission.url)
