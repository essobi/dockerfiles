FROM alpine:3.2  
# Install Nginx.  
RUN \  
apk add --update nginx && \  
rm -rf /var/cache/apk/*  
  
COPY nginx/nginx.conf /etc/nginx/nginx.conf  
COPY nginx/default.conf /etc/nginx/conf.d/default.conf  
COPY website /usr/share/nginx/html  
  
VOLUME ["/var/cache/nginx"]  
CMD ["nginx", "-g", "daemon off;"]  
EXPOSE 80  

