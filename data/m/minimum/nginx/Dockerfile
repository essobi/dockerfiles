FROM nginx:stable-alpine  
  
RUN apk add --update logrotate  
  
COPY nginx.conf /etc/logrotate.d/  
  
CMD crond && nginx -g "daemon off;"  

