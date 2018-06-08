FROM nginx  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
openssl \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/  
# Add ffdhe2048, ffdhe3072 and ffdhe4096 pre-defined DHE groups from RFC 7919.  
# See https://wiki.mozilla.org/Security/Server_Side_TLS#Pre-defined_DHE_groups  
ADD \  
dhparams.ffdhe2048.pem \  
dhparams.ffdhe3072.pem \  
dhparams.ffdhe4096.pem \  
/etc/ssl/private/  
  
# Create built-in 1024, 2048, 3072 & 4096 bit Diffie-Hellman Groups.  
# These are included for convenience. Make sure you understand the  
# implications of using them for production.  
# Since the image is public, they're not secret. USE AT YOUR OWN RISK!  
RUN \  
openssl dhparam -out /etc/ssl/private/dhparams.1024.pem 1024 && \  
openssl dhparam -out /etc/ssl/private/dhparams.2048.pem 2048 && \  
openssl dhparam -out /etc/ssl/private/dhparams.3072.pem 3072 && \  
openssl dhparam -out /etc/ssl/private/dhparams.4096.pem 4096 && \  
ln -vs /etc/ssl/private/dhparams.ffdhe2048.pem /etc/ssl/private/dhparams.pem  
  
ADD files/etc/nginx/conf.d/ /etc/nginx/conf.d/  
ADD files/etc/nginx/confs-available/ /etc/nginx/confs-available/  

