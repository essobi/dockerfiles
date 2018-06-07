FROM pataquets/ubuntu:xenial  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
hitch \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/  
# Create built-in 1024, 2048, 3072 & 4096 bit Diffie-Hellman Groups.  
# These are included for convenience. Make sure you understand the  
# implications of using them for production.  
# Since the image is public, they're not secret. USE AT YOUR OWN RISK!  
RUN \  
mkdir -vp /root/certs/ && \  
openssl dhparam -out /etc/ssl/private/dhparams.1024.pem 1024 && \  
openssl dhparam -out /etc/ssl/private/dhparams.2048.pem 2048 && \  
openssl dhparam -out /etc/ssl/private/dhparams.3072.pem 3072 && \  
openssl dhparam -out /etc/ssl/private/dhparams.4096.pem 4096 && \  
ln -vs /etc/ssl/private/dhparams.4096.pem /etc/ssl/private/dhparams.pem && \  
ln -vs /etc/ssl/private/dhparams.pem /root/certs/  
  
ENTRYPOINT [ "hitch" ]  
CMD [ "--help" ]  

