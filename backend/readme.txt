import base64
import re

def decode_base64(data, altchars=b'+/'):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    data = re.sub(rb'[^a-zA-Z0-9%s]+' % altchars, b'', data)  # normalize
    missing_padding = len(data) % 4
    if missing_padding:
        data += b'='* (4 - missing_padding)
    return base64.b64decode(data, altchars)
    
    
    
    https://readthedocs.org/projects/keycloak-client/downloads/pdf/latest/

https://auth0.com/blog/pt-how-to-handle-jwt-in-python/

https://medium.com/@agusnavce/authentication-is-hard-keycloak-to-the-rescue-32ca4b442a13

https://github.com/dangtrinhnt/keycloak_flask

https://github.com/search?q=flask+keycloak


docker run --rm  -p 3000:3000 --expose 3000 --mount type=bind,source=$PWD/app,target=/opt/webapp --name back kcback 


docker run --rm -p 3000:3000 --expose 3000 --mount type=bind,source=$PWD/app,target=/opt/webapp --name back pyback


docker run --rm  -p 8000:8000 --expose 8000 --name front kcfront



