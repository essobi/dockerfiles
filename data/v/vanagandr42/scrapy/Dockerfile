FROM lsiobase/alpine:70  
# Package version  
ARG SCRAPY_VER=1.4  
  
RUN apk add --no-cache \  
python3 \  
libxml2 \  
libxslt \  
py3-dateutil \  
libssl1.0 \  
&& apk add --no-cache --virtual=build-dependencies \  
python3-dev \  
gcc \  
musl-dev \  
openssl-dev \  
ca-certificates \  
libxml2-dev \  
libxslt-dev \  
libffi-dev \  
&& pip3 install scrapy \  
# Cleanup  
&& apk del --purge build-dependencies \  
&& rm -rf /tmp/*  
  
# Declare volumes  
VOLUME ["/config", \  
"/app"]  
  
WORKDIR /config  
  
ENTRYPOINT ["/init", "s6-setuidgid", "abc", "scrapy"]  
CMD ["--help"]

