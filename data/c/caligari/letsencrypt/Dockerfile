  
FROM debian:jessie  
  
LABEL maintainer "Rafa Couto <caligari@treboada.net>"  
  
# webroot to share with nginx container  
VOLUME /var/www/html  
  
# configuration  
VOLUME /etc/letsencrypt  
  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" \  
>> /etc/apt/sources.list.d/jessie-backports.list \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -qy --no-install-recommends
\  
-t jessie-backports certbot \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN echo 'webroot-path = /var/www/html' > /etc/letsencrypt/cli.ini  
  
WORKDIR /var/www/html  
  
# default command  
CMD certbot renew  
  

