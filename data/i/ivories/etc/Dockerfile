FROM ivories/etc  
  
RUN apk add --no-cache nginx  
RUN sed -i "s#pcre_jit on;#pid /run/nginx.pid;#g" /etc/nginx/nginx.conf  
RUN apk add --no-cache bash  
  
ENTRYPOINT []  

