FROM alpine:3.6  
LABEL maintainer="Javier <kilwacero@gmail.com>"  
  
ADD pkt.tar.gz /  
  
RUN apk add --no-cache nginx libressl && \  
mkdir /run/nginx && \  
rm -rf /etc/nginx && \  
mv /nginx /etc && \  
mv /run.sh /usr/sbin/ && \  
openssl dhparam -dsaparam -out /etc/nginx/dhparam.pem 4096 && \  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
ENV TOKEN "token"  
EXPOSE 443 80  
STOPSIGNAL SIGTERM  
  
CMD ["/usr/sbin/run.sh"]  

