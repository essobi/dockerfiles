FROM ubuntu:yakkety  
MAINTAINER jakendall@gmail.com  
  
RUN apt-get update && apt-get install -yq build-essential libpcre3
libpcre3-dev libssl-dev unzip curl ffmpeg && apt-get clean && rm -rf
/var/lib/apt/lists/* /var/tmp/* /tmp/*  
  
RUN mkdir /root/workdir /root/workdir/nginx  
  
WORKDIR /root/workdir  
  
RUN curl -sSL http://nginx.org/download/nginx-1.7.5.tar.gz | tar -zxv -C
/root/workdir/nginx --strip-components=1  
RUN curl -sSL https://github.com/arut/nginx-rtmp-module/archive/master.zip -o
master.zip  
RUN unzip master.zip  
  
WORKDIR /root/workdir/nginx  
  
RUN ./configure --with-http_ssl_module --add-module=../nginx-rtmp-module-
master  
  
RUN make -j4 && make install  
ADD nginx.conf /usr/local/nginx/conf/nginx.conf  
  
WORKDIR /usr/local/nginx  
  
CMD ["sbin/nginx"]  
  
EXPOSE 1935  

