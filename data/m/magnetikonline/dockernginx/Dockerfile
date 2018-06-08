FROM ubuntu:16.04  
MAINTAINER Peter Mescalchin <peter@magnetikonline.com>  
  
ENV VERSION 1.12.2  
RUN apt-get update && apt-get upgrade --yes && \  
apt-get install --yes gcc libpcre3-dev make zlib1g-dev && \  
apt-get clean  
  
ADD https://nginx.org/download/nginx-$VERSION.tar.gz /root/build/  
WORKDIR /root/build  
RUN tar -xf nginx-$VERSION.tar.gz  
  
ADD ./resource/configure.sh /root/build/nginx-$VERSION/  
WORKDIR /root/build/nginx-$VERSION  
  
RUN chmod u+x configure.sh  
RUN ./configure.sh && \  
make --ignore-errors install  
  
VOLUME ["/etc/nginx","/srv/http","/var/log/nginx"]  
  
EXPOSE 80 443  
CMD ["/usr/local/sbin/nginx"]  

