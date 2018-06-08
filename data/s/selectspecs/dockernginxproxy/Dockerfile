FROM alpine:latest  
RUN apk add --no-cache nginx  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr
/var/log/nginx/error.log  
ADD ./nginx.conf /etc/nginx/nginx.conf  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

