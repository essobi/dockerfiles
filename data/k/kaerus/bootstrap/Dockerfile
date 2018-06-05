FROM microsoft/dotnet  
  
COPY . /.bootstrap/  
WORKDIR /.bootstrap  
  
RUN apt-get update && \  
apt-get install -y cmake nasm wget git g++ xz-utils  
  
RUN wget
https://github.com/libgd/libgd/releases/download/gd-2.1.1/libgd-2.1.1.tar.gz
&& \  
tar -xvzf libgd-2.1.1.tar.gz && \  
cd libgd-2.1.1 && \  
./thumbs.sh make || true && \  
cd .. && \  
rm -r libgd-2.1.1  
  
RUN wget http://johnvansickle.com/ffmpeg/releases/ffmpeg-release-64bit-
static.tar.xz && \  
mkdir ffmpeg && \  
tar xf ffmpeg-release-64bit-static.tar.xz -C ffmpeg --strip-components=1 && \  
rm ffmpeg-release-64bit-static.tar.xz  
  
RUN apt-get -qqy install wget make && \  
mkdir -p /tmp/cache && \  
mkdir build-nginx && \  
cd build-nginx && \  
wget http://www.openssl.org/source/openssl-1.0.2g.tar.gz && \  
wget http://www.zlib.net/fossils/zlib-1.2.8.tar.gz && \  
wget http://nginx.org/download/nginx-1.9.12.tar.gz && \  
tar -xvzf openssl-1.0.2g.tar.gz && \  
tar -xvzf zlib-1.2.8.tar.gz && \  
tar -xvzf nginx-1.9.12.tar.gz && \  
cd nginx-1.9.12 && \  
./configure --prefix=/etc/nginx --sbin-path=/usr/sbin/nginx --with-
zlib=../zlib-1.2.8 --without-http_rewrite_module --with-http_ssl_module
--with-http_v2_module --with-debug --with-openssl=../openssl-1.0.2g && \  
make && \  
make install && \  
rm /etc/nginx/conf/nginx.conf  
  
RUN dotnet restore  

