FROM alpine:3.7  
RUN apk add --no-cache openssl  
  
COPY *.cnf root-ca.crt root-ca.key /srv/  
  
WORKDIR /ssl  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

