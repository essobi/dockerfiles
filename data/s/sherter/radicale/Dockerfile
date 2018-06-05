FROM python:3-alpine  
  
ENV RADICALE_VERSION 1.1.1  
  
RUN set -xe \  
&& addgroup -S radicale \  
&& adduser -D -S -h /radicale -s /sbin/nologin -G radicale radicale \  
&& apk add \--no-cache --virtual .build-deps \  
gcc \  
musl-dev \  
libffi-dev \  
&& pip install -v --no-cache-dir --disable-pip-version-check \  
radicale==$RADICALE_VERSION \  
# md5 and bcrypt support for htpasswd access  
passlib bcrypt \  
&& apk add \--no-cache --virtual .runtime-deps \  
# required by bcrypt  
libffi \  
&& apk del .build-deps  
  
EXPOSE "5232"  
USER "radicale"  
ENTRYPOINT ["radicale"]  
CMD ["--foreground"]  

