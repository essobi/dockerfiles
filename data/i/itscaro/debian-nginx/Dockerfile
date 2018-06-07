FROM itscaro/debian-ssh:latest  
  
MAINTAINER Minh-Quan TRAN "account@itscaro.me"  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62  
RUN echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list  
  
ENV NGINX_VERSION 1.9.5-1~jessie  
  
RUN apt-get update && \  
apt-get install -y ca-certificates nginx=${NGINX_VERSION} && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean  
  
ADD index.html /var/www/html/index.html  
ADD default.conf /etc/nginx/conf.d/default.conf  
ADD start.sh /start.sh  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
VOLUME ["/var/cache/nginx", "/var/www/"]  
  
EXPOSE 80 443  
ENTRYPOINT ["/start.sh"]  
  
#CMD [""]

