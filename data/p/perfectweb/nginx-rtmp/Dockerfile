FROM centos:latest  
MAINTAINER Alin Jurj <office@perfectweb.ro>  
  
RUN yum -y install http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-
release-0-5.el7.nux.noarch.rpm  
RUN yum -y update  
RUN yum install -y pcre-devel zlib-devel openssl-devel unzip ffmpeg wget  
RUN yum groupinstall 'Development Tools' -y  
RUN mkdir -p /sources/nginx  
RUN mkdir -p /sources/rtmp  
RUN wget -O nginx.zip https://github.com/nginx/nginx/archive/master.zip  
RUN wget -O rtmp.zip https://github.com/arut/nginx-rtmp-
module/archive/master.zip  
RUN unzip nginx.zip -d /sources/nginx  
RUN unzip rtmp.zip -d /sources/rtmp  
RUN ls -lrt /sources/rtmp/nginx-rtmp-module-master  
RUN cd /sources/nginx/nginx-master && ./configure --add-
module=/sources/rtmp/nginx-rtmp-module-master --with-http_ssl_module  
RUN cd /sources/nginx/nginx-master && make && make install  
RUN echo "daemon off;" >> /usr/local/nginx/conf/nginx.conf  
  
ENV PATH /usr/local/nginx/sbin/:$PATH  
ENV NGINX_HOME /usr/local/nginx/  
  
WORKDIR /usr/local/nginx  
EXPOSE 80 1935  
CMD nginx -c /usr/local/nginx/conf/nginx.conf

