FROM alpine:3.4  
MAINTAINER Nathon Fowlie <nathon.fowlie@gmail.com>  
  
EXPOSE 443  
WORKDIR /tmp  
  
ARG SAN="DNS:localhost,IP:127.0.0.1"  
ARG SUBJECT="/C=AU/ST=NSW/L=Sydney/O=Localhost/CN=localhost"  
ARG CN="localhost"  
# Install OpenSSL and setup the directory structure for the public & private
keys  
RUN apk update && apk upgrade && apk add openssl \  
&& mkdir -p /etc/ssl/private \  
&& mkdir -p /etc/ssl/cer \  
&& chmod -R 640 /etc/ssl/private \  
&& chmod -R 644 /etc/ssl/cer  
  
# Generate the root CA and self signed SSL certificates, using random
passwords  
ADD files/ssl/openssl.cnf openssl.cnf  
  
RUN touch rootCA.pass ${CN}_in.pass ${CN}_out.pass \  
&& chmod 600 rootCA.pass ${CN}_in.pass ${CN}_out.pass \  
&& dd if=/dev/urandom bs=1 count=20 2>/dev/null | base64 >> rootCA.pass \  
&& dd if=/dev/urandom bs=1 count=20 2>/dev/null | base64 >> ${CN}_out.pass \  
&& dd if=/dev/urandom bs=1 count=20 2>/dev/null | base64 >> ${CN}_in.pass \  
&& openssl genrsa -aes256 -out /etc/ssl/private/rootCA.key -passout
file:rootCA.pass 4096 \  
&& openssl req -x509 -new -extensions v3_ca -key /etc/ssl/private/rootCA.key
-sha256 -days 365 -out /etc/ssl/cer/rootCA.crt -passin file:rootCA.pass -subj
/C=AU/ST=NSW/L=Sydney/O=Localhost/CN=localhost \  
&& env 'subjectAltName=${SAN}' openssl req -new -nodes -x509 -newkey rsa:4096
-keyout /etc/ssl/private/localhost.key -out /etc/ssl/cer/localhost.crt -days
365 -passin file:${CN}_in.pass -passout file:${CN}_out.pass -subj ${SUBJECT}
-config openssl.cnf \  
&& rm *.pass *.cnf  
  
# Add the website that will be served by NGINX  
ADD files/data /data  
  
# Install and configure NGINX  
RUN apk add nginx \  
&& mkdir -p /etc/nginx/conf.d \  
&& chmod -R 755 /data/www/public_html \  
&& mkdir -p /run/nginx  
  
ADD files/etc/nginx/nginx.conf /etc/nginx/nginx.conf  
ADD files/etc/nginx/conf.d/localhost.conf /etc/nginx/conf.d/localhost.conf  
  
ENTRYPOINT ["/usr/sbin/nginx"]

