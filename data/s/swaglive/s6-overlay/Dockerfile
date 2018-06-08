FROM alpine:3.7  
ENV VERSION=1.21.4.0  
RUN apk add --no-cache --virtual .build-deps \  
curl && \  
curl -fSL https://github.com/just-
containers/s6-overlay/releases/download/v$VERSION/s6-overlay-amd64.tar.gz |
tar xz && \  
apk del .build-deps  
ENTRYPOINT ["/init"]  

