FROM alpine:edge  
  
RUN echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
  
# Install nginx package and remove cache  
RUN apk add --update nginx && rm -rf /var/cache/apk/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
# Copy basic files  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY default.conf /etc/nginx/conf.d/default.conf  
  
EXPOSE 80 443  
VOLUME ["/code"]  
  
CMD ["nginx", "-g", "daemon off;"]

