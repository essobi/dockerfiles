FROM gjchen/alpine:edge  
  
RUN echo '@testing http://nl.alpinelinux.org/alpine/edge/testing' >>
/etc/apk/repositories && \  
apk --no-cache --no-progress upgrade -f && \  
apk --no-cache --no-progress add nginx curl && \  
mkdir -p /etc/nginx/server.d  
  
ADD nginx-main.conf /etc/nginx/modules/main.conf  
ADD nginx-http.conf /etc/nginx/conf.d/00-http.conf  
ADD default.conf /etc/nginx/conf.d/default.conf  
ADD https://raw.githubusercontent.com/lukas2511/dehydrated/master/dehydrated
/etc/ssl/  
ADD letsencrypt-ca-certs.pem /etc/ssl/  
ADD s6.d /etc/s6.d  
  
# support Lets Encrypt, renew automatically  
RUN mkdir -p /var/log/nginx && \  
chmod 755 /var/log/nginx && \  
rm -f /var/log/nginx/* && \  
ln -s /dev/null /var/log/nginx/access.log && \  
ln -s /dev/null /var/log/nginx/error.log && \  
cd /etc/ssl && \  
mkdir -p .acme-challenges certs.d/default && \  
#wget -O - https://letsencrypt.org/certs/isrgrootx1.pem
https://letsencrypt.org/certs/lets-encrypt-x1-cross-signed.pem
https://letsencrypt.org/certs/letsencryptauthorityx1.pem
https://www.identrust.com/certificates/trustid/root-download-x3.html | tee -a
letsencrypt-ca-certs.pem && \  
openssl dhparam -out dh2048.pem 2048 && \  
chmod a+x dehydrated && \  
printf "WELLKNOWN=/etc/ssl/.acme-challenges\nCERTDIR=/etc/ssl/certs.d\n" >
config && \  
echo '0 0 * * * sleep $(expr $(printf "%d" "0x$(hostname | md5sum | cut -c
1-8)") \% 86400);/etc/ssl/dehydrated -c --ocsp; nginx -s reload' >>
/etc/crontabs/root  
  
EXPOSE 80 443  

