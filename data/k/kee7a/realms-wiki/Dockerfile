FROM alpine  
  
RUN apk update && \  
apk add \  
python-dev \  
openldap-dev \  
libsasl \  
libressl2.6-libssl \  
yaml-dev \  
libffi \  
zlib-dev \  
libxslt-dev \  
libxml2-dev \  
py-pip \  
py-cffi \  
musl-dev \  
gcc \  
bash && \  
rm -rf \  
/var/cache/apk/*  
  
RUN pip install realms-wiki && \  
rm -rf \  
/root/.cache/pip  
  
RUN addgroup \  
-S -g 1000 \  
wiki && \  
adduser \  
-S -H -D \  
-h /data \  
-s /bin/bash \  
-u 1000 \  
-G wiki \  
  
USER wiki  
  
ENV WORKERS=3  
ENV GEVENT_RESOLVER=ares  
ENV REALMS_ENV=docker  
ENV REALMS_WIKI_PATH=/data/wiki/repo  
ENV REALMS_DB_URI='sqlite:////data/db/wiki.db'  
  
VOLUME /data/config  
VOLUME /data/db  
VOLUME /data/wiki  
  
EXPOSE 5000  
  
WORKDIR /data/config  
  
CMD gunicorn \  
\--name realms-wiki \  
\--access-logfile - \  
\--error-logfile - \  
\--worker-class gevent \  
\--workers ${WORKERS} \  
\--bind 0.0.0.0:5000 \  
'realms:create_app()'  

