FROM debian:jessie  
MAINTAINER Gabriel Eckerson 014@savemetechs.net  
  
RUN apt-get update && \  
apt-get upgrade -y  
  
RUN apt-get -y install build-essential libpcre3 libpcre3-dev libssl-dev wget
unzip && \  
mkdir /usr/build && \  
cd /usr/build && \  
wget http://nginx.org/download/nginx-1.9.9.tar.gz && \  
wget https://github.com/arut/nginx-rtmp-module/archive/master.zip && \  
wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-64bit-
static.tar.xz && \  
tar -xvf nginx-1.9.9.tar.gz && \  
unzip master.zip && \  
tar -xvf ffmpeg-release-64bit-static.tar.xz && \  
cd nginx-1.9.9 && \  
./configure --with-http_ssl_module --add-module=../nginx-rtmp-module-master &&
\  
make && \  
make install  
  
RUN mkdir /usr/local/nginx/html/stream && \  
mkdir /usr/local/nginx/html/stream/vids && \  
mkdir /usr/local/nginx/html/stream/css && \  
mkdir /usr/local/nginx/html/stream/images  
  
COPY nginx.conf /usr/local/nginx/conf/nginx.conf  
COPY index.html vlc.html /usr/local/nginx/html/stream/  
COPY css /usr/local/nginx/html/stream/css/  
EXPOSE 1935 80  
CMD ["/usr/local/nginx/sbin/nginx"]  

