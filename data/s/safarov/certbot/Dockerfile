FROM nginx:1.12.1-alpine  
  
ADD entrypoint.sh /  
RUN apk --no-cache add certbot  
  
ENTRYPOINT ["/entrypoint.sh"]  

