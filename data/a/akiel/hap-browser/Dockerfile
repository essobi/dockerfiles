FROM debian:jessie  
  
##  
## This is a copy from https://github.com/nginxinc/docker-
nginx/blob/master/Dockerfile  
##  
## I need to fork it because I can only expose on port so that the container
works in Deis.  
## https://github.com/deis/deis/issues/1156  
##  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62  
RUN echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list  
  
ENV NGINX_VERSION 1.9.3-1~jessie  
  
RUN apt-get update && \  
apt-get install -y ca-certificates nginx=${NGINX_VERSION} && \  
rm -rf /var/lib/apt/lists/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
VOLUME ["/var/cache/nginx"]  
  
EXPOSE 80  
RUN rm /usr/share/nginx/html/*  
COPY resources/public/css /usr/share/nginx/html/css  
COPY resources/public/fonts /usr/share/nginx/html/fonts  
ADD https://s3.eu-central-1.amazonaws.com/hap-browser/hap-browser.js
/usr/share/nginx/html/js/  
RUN chmod 644 /usr/share/nginx/html/js/hap-browser.js  
COPY resources/public/index.html /usr/share/nginx/html/  
  
COPY docker/nginx.conf /etc/nginx/  
COPY docker/default.conf /etc/nginx/conf.d/  
COPY docker/start.sh /  
RUN chmod +x /start.sh  
  
CMD ["/start.sh"]  

