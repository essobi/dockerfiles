FROM nginx:stable-alpine  
  
  
RUN apk update && apk add curl openssl && rm -Rf /var/cache/apk/*  
  
RUN rm -Rf /etc/nginx/conf.d/*  
  
ADD entrypoint.sh /opt/entrypoint.sh  
  
ENTRYPOINT ["/opt/entrypoint.sh"]  
  

