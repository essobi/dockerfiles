FROM alpine  
  
ENV DOMAIN localhost  
  
ENTRYPOINT ["/entrypoint"]  
  
RUN apk -U add openssl && \  
rm -rf /var/cache/apk/*  
  
COPY entrypoint /entrypoint  
COPY mksslcert /usr/bin/mksslcert  

