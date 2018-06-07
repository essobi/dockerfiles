FROM alpine  
  
MAINTAINER Ryan Roberts <ryansroberts@gmail.com>  
  
# Install Nginx.  
RUN apk add --update nginx && rm -rf /var/cache/apk/*  
  
# Define mountable directories.  
VOLUME ["/etc/nginx/certs", "/etc/nginx/conf.d", "/var/log/nginx"]  
  
# Define working directory.  
WORKDIR /etc/nginx  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log && \  
rm -rf /usr/share/nginx/html/* && \  
rm -f /etc/nginx/mime.types && \  
chown -R nginx:nginx /var/lib/nginx/ &&\  
chown -R nginx:nginx /var/www  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY default.conf /etc/nginx/conf.d/default.conf  
COPY mime.types /etc/nginx/  
COPY index.html /var/www/viewer/  
COPY style.css /var/www/viewer/  
  
RUN ln -s /artifacts /var/www/viewer  
# Define default command.  
CMD ln -sf /dev/stdout /var/log/nginx/access.log &&\  
ln -sf /dev/stderr /var/log/nginx/error.log &&\  
nginx  
# Expose ports.  
EXPOSE 80  
EXPOSE 443  

