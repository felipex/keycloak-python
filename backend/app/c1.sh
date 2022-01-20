curl \
  -d "client_id=myclient" \
  -d "username=felipe" \
  -d "password=123456" \
  -d "grant_type=password" \
  "http://localhost:8080/auth/realms/myrealm/protocol/openid-connect/token"
