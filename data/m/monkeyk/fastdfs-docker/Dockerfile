# Pull base image  
FROM hub.c.163.com/library/centos:6.8  
MAINTAINER zjg23 "zhaojianguo1234@aliyun.com"  
#install dependency  
RUN yum install -y zlib zlib-devel pcre pcre-devel gcc gcc-c++ openssl
openssl-devel libevent libevent-devel perl unzip  
  
#install libfastcommon  
ADD libfastcommon-1.0.7.zip /usr/local/src/  
RUN cd /usr/local/src \  
&& unzip /usr/local/src/libfastcommon-1.0.7.zip \  
&& cd libfastcommon-1.0.7 \  
&& ./make.sh \  
&& ./make.sh install  
  
#install fastdfs  
ADD FastDFS_v5.05.tar.gz /usr/local/src/  
RUN cd /usr/local/src/FastDFS \  
&& ./make.sh \  
&& ./make.sh install \  
&& cp conf/*.conf /etc/fdfs \  
&& cd /etc/fdfs/ \  
&& rm -rf *.sample  
  
#install nginx  
ADD fastdfs-nginx-module_v1.16.tar.gz /usr/local/src/  
ADD nginx-1.7.8.tar.gz /usr/local/src/  
RUN cd /usr/local/src/ \  
&& cd nginx-1.7.8 \  
&& ./configure --prefix=/usr/local/nginx --add-module=/usr/local/src/fastdfs-
nginx-module/src \  
&& make \  
&& make install \  
&& cp /usr/local/src/fastdfs-nginx-module/src/mod_fastdfs.conf /etc/fdfs/  
ADD nginx.conf /usr/local/nginx/conf/  
  
#create directory  
RUN mkdir -p /export/fastdfs/{storage,tracker}  
ADD tracker.sh /usr/local/src/  
ADD storage.sh /usr/local/src/  

