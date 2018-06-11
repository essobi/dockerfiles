FROM ubuntu:xenial  
  
RUN apt-get update  
  
# http://openresty.org/en/linux-packages.html  
RUN apt-get -y install software-properties-common && \  
add-apt-repository -y ppa:openresty/ppa && \  
apt-get update && \  
apt-get install -y openresty  
  
EXPOSE 80  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /usr/local/openresty/nginx/logs/access.log \  
&& ln -sf /dev/stderr /usr/local/openresty/nginx/logs/error.log  
  
COPY nginx.conf /usr/local/openresty/nginx/conf/  
  
CMD ["openresty", "-g", "daemon off;"]  

