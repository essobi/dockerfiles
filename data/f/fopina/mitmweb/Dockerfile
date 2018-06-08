# arm32v6/python:3.6.4-alpine3.7  
ARG BASEIMG=python:3.6.5-alpine3.7  
FROM $BASEIMG as builder  
  
RUN apk add --no-cache build-base libffi-dev openssl-dev  
RUN pip wheel -w /dist
https://github.com/mitmproxy/mitmproxy/archive/v3.0.4.tar.gz  
  
FROM $BASEIMG  
  
# Expose ports  
# - 8080: Default mitmproxy port  
# - 8081: Default mitmweb port  
EXPOSE 8080  
EXPOSE 8081  
COPY \--from=builder /dist /wheels  
  
RUN apk add --no-cache libffi libssl1.0  
RUN pip install --no-index --find-links=/wheels
/wheels/mitmproxy-3.0.4-py3-none-any.whl  
  
# Location of the default mitmproxy CA files  
VOLUME [ "/ca" ]  
  
ENTRYPOINT [ "/usr/local/bin/mitmweb", "--set", "cadir=/ca", "--web-iface",
"0.0.0.0" ]

