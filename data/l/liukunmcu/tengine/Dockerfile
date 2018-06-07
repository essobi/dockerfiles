FROM debian:wheezy  
  
MAINTAINER liukunmcu "lkmcudevelope@gmail.com"  
WORKDIR /tengine  
ADD . /tengine  
RUN apt-get update  
RUN apt-get -y install build-essential  
RUN apt-get -y install libpcre3 libpcre3-dev libpcrecpp0 libssl-dev zlib1g-dev  
RUN ./configure  
RUN make  
RUN make install  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /usr/local/nginx/logs/access.log  
RUN ln -sf /dev/stderr /usr/local/nginx/logs/error.log  
WORKDIR /usr/local/nginx/sbin  
VOLUME ["/var/cache/nginx"]  
  
EXPOSE 80 443  
CMD ["./nginx", "-g", "daemon off;"]  

