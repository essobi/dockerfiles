FROM python:3.6-alpine3.6  
ENTRYPOINT [ "certbot" ]  
EXPOSE 80 443  
VOLUME /etc/letsencrypt /var/lib/letsencrypt  
WORKDIR /opt/certbot  
  
COPY CHANGES.rst README.rst setup.py src/  
COPY acme src/acme  
COPY certbot src/certbot  
COPY certbot-dns-route53 src/certbot-dns-route53  
  
RUN apk add --no-cache --virtual .certbot-deps \  
libffi \  
libssl1.0 \  
openssl \  
ca-certificates \  
binutils  
RUN apk add --no-cache --virtual .build-deps \  
gcc \  
linux-headers \  
openssl-dev \  
musl-dev \  
libffi-dev \  
&& pip install --no-cache-dir \  
\--editable /opt/certbot/src/acme \  
\--editable /opt/certbot/src \  
\--editable /opt/certbot/src/certbot-dns-route53 \  
&& apk del .build-deps  

