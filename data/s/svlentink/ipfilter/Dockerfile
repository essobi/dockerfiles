FROM nginx:alpine  
RUN apk add --no-cache openssl  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  

