FROM ubuntu:wily  
  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62  
RUN echo "deb http://nginx.org/packages/mainline/ubuntu/ wily nginx" >>
/etc/apt/sources.list  
  
ENV NGINX_VERSION 1.9.8-1~wily  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends ca-certificates
nginx=${NGINX_VERSION} && \  
rm -rf /var/lib/apt/lists/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
COPY ./config/proxy.conf /etc/nginx/conf.d/  
  
VOLUME ["/var/cache/nginx"]  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

