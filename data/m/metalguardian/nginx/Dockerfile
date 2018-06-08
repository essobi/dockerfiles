FROM ubuntu:14.04.3  
MAINTAINER Ivan Pushkin <imetalguardi+docker@gmail.com>  
  
ENV TERM xterm  
  
# add nginx repository  
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62  
RUN echo "deb http://nginx.org/packages/mainline/ubuntu/ $(lsb_release -cs)
nginx" > /etc/apt/sources.list.d/nginx.list  
  
ENV NGINX_VERSION 1.9.*  
  
# update  
RUN apt-get update  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y -q --no-install-recommends
install \  
ca-certificates \  
nginx=${NGINX_VERSION}  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80 443  
VOLUME ["/var/cache/nginx"]  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["nginx", "-g", "daemon off;"]  

