FROM gjchen/php7:base  
MAINTAINER gjchen <gjchen.tw@gmail.com>  
  
RUN echo '@testing http://nl.alpinelinux.org/alpine/edge/testing' >>
/etc/apk/repositories && \  
apk --no-cache --no-progress upgrade -f && \  
apk --no-cache --no-progress add nginx curl postfix && \  
mkdir -p /etc/nginx/server.d  
  
ADD nginx-main.conf /etc/nginx/modules/main.conf  
ADD nginx-http.conf /etc/nginx/conf.d/00-http.conf  
ADD nginx-default-server.conf /etc/nginx/conf.d/default.conf  
ADD https://raw.githubusercontent.com/lukas2511/dehydrated/v0.3.1/dehydrated
/etc/ssl/  
ADD letsencrypt-ca-certs.pem /etc/ssl/  
ADD s6.d /etc/s6.d  
  
# support Lets Encrypt, renew automatically if CRON_ENABLED=1  
RUN mkdir -p /var/log/nginx && \  
chmod 755 /var/log/nginx && \  
rm -f /var/log/nginx/* && \  
ln -s /dev/null /var/log/nginx/access.log && \  
ln -s /dev/null /var/log/nginx/error.log && \  
cd /etc/ssl && \  
mkdir -p .acme-challenges certs.d/default && \  
openssl dhparam -out dh2048.pem 2048 && \  
chmod a+x dehydrated && \  
printf "WELLKNOWN=/etc/ssl/.acme-challenges\nCERTDIR=/etc/ssl/certs.d\n" >
config && \  
echo '0 0 * * * sleep $(expr $(printf "%d" "0x$(hostname | md5sum | cut -c
1-8)") \% 86400);/etc/ssl/dehydrated -c --ocsp; nginx -s reload' >>
/etc/crontabs/root && \  
mkdir -p /var/spool/postfix/etc && \  
echo nameserver 8.8.8.8 > /var/spool/postfix/etc/resolv.conf  
  
VOLUME [ "/app", "/etc/nginx/server.d", "/etc/ssl/certs.d", "/etc/ssl/.acme-
challenges", "/etc/ssl/accounts" ]  
  
EXPOSE 80 443  

