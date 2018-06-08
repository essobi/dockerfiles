FROM nginx:stable  
  
LABEL maintainer "Backend Team <backend@socialpoint.es>"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
COPY ssl.conf /tmp/  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
openssl \  
apt-utils \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN openssl genrsa -des3 -out /etc/ssl/private/myssl.key -passout
pass:abcd1234 1024 \  
&& openssl req -new -key /etc/ssl/private/myssl.key -out /tmp/myssl.csr
-config /tmp/ssl.conf -passin pass:abcd1234 \  
&& openssl rsa -in /etc/ssl/private/myssl.key -out /etc/ssl/private/myssl.key
-passin pass:abcd1234 \  
&& openssl x509 -req -days 1825 -extensions usr_cert -in /tmp/myssl.csr
-signkey /etc/ssl/private/myssl.key -out /etc/ssl/certs/myssl.crt \  
&& rm /tmp/ssl.conf /tmp/myssl.csr  
  
RUN rm /etc/nginx/conf.d/default.conf  
  
RUN sed -i 's/^worker_processes.*/worker_processes auto;/'
/etc/nginx/nginx.conf  
  
COPY nginx.conf /etc/nginx/conf.d/  

