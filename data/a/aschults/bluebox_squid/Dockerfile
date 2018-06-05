FROM alpine  
#RUN sed -i -e 's/v3\\.[0-9][0-9]*/edge/g' /etc/apk/repositories  
RUN apk update && apk add squid gettext openssl ca-certificates lighttpd curl  
RUN update-ca-certificates  
  
EXPOSE 3128  
RUN mkdir -p /var/spool/squid/cache /var/log/squid /etc/squid/conf_custom.d ;
chown -R squid:squid /var/spool/squid/cache /var/log/squid  
VOLUME ["/var/spool/squid/cache", "/var/log/squid", "/var/spool/squid/ssl",
"/etc/squid/conf_custom.d"]  
  
COPY conf /etc/squid/  
ADD squid.sh /  
ADD lib.sh /  
  
ADD lighttpd/lighttpd.conf /etc/lighttpd/  
ADD lighttpd/index.html /var/www/localhost/htdocs  
  
ADD liveness_check.sh /  
ARG SSL_CA_CERTS  
RUN if [ -n "$SSL_CA_CERTS" ] ; then echo "$SSL_CA_CERTS" >
/usr/local/share/ca-certificates/__testserver.crt ; update-ca-certificates
--fresh ; fi  
  
ENTRYPOINT sh squid.sh  

