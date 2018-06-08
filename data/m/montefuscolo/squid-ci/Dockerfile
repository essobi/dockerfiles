FROM alpine  
MAINTAINER fabio.montefuscolo@gmail.com  
  
RUN apk update \  
&& apk add openssl squid \  
&& rm -rf /var/cache/apk/* \  
&& { \  
echo ''; \  
echo '[ v3_req ]'; \  
echo 'basicConstraints = CA:FALSE'; \  
echo 'keyUsage = nonRepudiation, digitalSignature, keyEncipherment'; \  
echo ''; \  
echo '[ v3_ca ]'; \  
echo 'keyUsage = cRLSign, keyCertSign'; \  
} >> /etc/ssl/openssl.cnf  
  
COPY squid.conf /etc/squid/squid.conf  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
EXPOSE 3128/tcp  
VOLUME ["/var/cache/squid", "/etc/squid/ssl_cert", "/var/lib/squid"]  
ENTRYPOINT ["/sbin/entrypoint.sh"]  
CMD ["/usr/sbin/squid", "-f", "/etc/squid/squid.conf", "-NYCd", "1"]  
  

