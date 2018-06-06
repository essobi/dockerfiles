FROM docker.io/python:2-alpine3.7  
ARG VERSION=0.30.0  
ADD "https://github.com/matrix-org/synapse/archive/v$VERSION.tar.gz" /  
RUN tar -xf "/v$VERSION.tar.gz" && mv /synapse-$VERSION/ /synapse  
WORKDIR /synapse  
  
RUN apk add --no-cache su-exec libffi zlib zlib libressl libjpeg-turbo libpq
libxslt \  
&& apk add --no-cache --virtual .build_deps build-base libffi-dev zlib-dev
libressl-dev libjpeg-turbo-dev linux-headers postgresql-dev libxslt-dev \  
&& pip install --no-cache-dir --upgrade pip setuptools psycopg2 lxml \  
&& pip install --no-cache-dir --upgrade --process-dependency-links . \  
&& mv /synapse/contrib/docker/start.py /synapse/contrib/docker/conf / \  
&& apk del --purge .build_deps  
  
VOLUME ["/data"]  
  
EXPOSE 8008/tcp 8448/tcp  
  
ENTRYPOINT ["/start.py"]

