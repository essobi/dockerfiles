# Define the base image  
FROM centos:latest  
# Setting up the folders  
RUN mkdir /root/soft && \  
mkdir /root/src && \  
mkdir /root/config && \  
mkdir /root/web && \  
mkdir /root/web/html && \  
mkdir /root/soft/tengine && \  
mkdir /root/soft/senginx && \  
mkdir /root/soft/nginx && \  
mkdir /root/web/hls && \  
mkdir /root/web/vod && \  
mkdir /root/web/dash && \  
mkdir /root/web/hls/transcode && \  
mkdir /root/web/dash/transcode && \  
mkdir /root/web/record && \  
ln -s /root/web/record /root/web/html/record && \  
mkdir /root/soft/ffmpeg && \  
mkdir /root/logs && \  
mkdir /root/shell  
# Add the config and shell files  
ADD conf /root/config  
ADD html /root/web/html  
ADD shell /root/shell  
# Nginx version.You can change this according to the offical website  
ENV nginx_ver=1.13.8  
# Which module would you compile  
ENV mod_comp=http-flv  
# YASM version  
ENV yasmver=1.3.0  
# Node.js version  
ENV node_series=v8.x  
ENV node_ver=v8.9.4  
# Environment settingup  
RUN yum install -y zlib zlib-devel openssl* pcre pcre-devel git bash psmisc
wget autoconf automake \  
make gcc gcc-c++ patch pkgconfig libtool nasm nasm* freetype* && \  
# Clean the downloaded packages  
yum clean all && \  
# Clone the source code  
cd /root/src && \  
git clone https://github.com/FFmpeg/FFmpeg.git && \  
#git clone https://github.com/NeusoftSecurity/SEnginx.git && \  
git clone https://github.com/arut/nginx-rtmp-module.git && \  
git clone https://github.com/winshining/nginx-http-flv-module.git && \  
wget http://nginx.org/download/nginx-$nginx_ver.tar.gz && \  
tar -xzf nginx-$nginx_ver.tar.gz && \  
# Copy module src  
#cp -r nginx-rtmp-module ./SEnginx && \  
cp -r nginx-rtmp-module ./nginx-$nginx_ver && \  
cp -r nginx-http-flv-module ./SEnginx && \  
cp -r nginx-http-flv-module ./nginx-$nginx_ver && \  
# Compiling nginx  
#cd /root/src/SEnginx && \  
#./configure --prefix=/root/soft/senginx --with-http_ssl_module #--add-
module=./nginx-$mod_comp-module && \  
#make -j4 && \  
#make install && \  
cd /root/src/nginx-$nginx_ver && \  
./configure \--prefix=/root/soft/nginx \--with-http_ssl_module \--add-
module=./nginx-$mod_comp-module && \  
make -j4 && \  
make install && \  
# Create soft links  
cd /root && \  
ln -s /root/soft/nginx/conf /root/config/nginx_conf && \  
#ln -s /root/soft/senginx/conf /root/config/senginx_conf && \  
ln -s /root/soft/nginx/logs /root/logs/nginx_logs && \  
#ln -s /root/soft/senginx/logs /root/logs/senginx_logs && \  
# Backup the default conf file  
mv /root/soft/nginx/conf/nginx.conf /root/soft/nginx/conf/nginx.conf.bak && \  
#mv /root/soft/senginx/conf/nginx.conf /root/soft/senginx/conf/nginx.conf.bak
&& \  
# Setting up compile environment for FFmpeg  
cd /root/src && \  
# Install YASM  
wget http://www.tortall.net/projects/yasm/releases/yasm-$yasmver.tar.gz && \  
tar -zxvf yasm-$yasmver.tar.gz && \  
cd yasm-$yasmver && \  
./configure \--prefix=/usr && \  
make -j4 && \  
make install && \  
# Install libx264  
cd /root/src && \  
git clone \--depth 1 http://git.videolan.org/git/x264 && \  
cd x264 && \  
PKG_CONFIG_PATH="/root/soft/ffmpeg/lib/pkgconfig" ./configure \  
\--prefix="/root/soft/ffmpeg" \--bindir="/root/soft/ffmpeg/bin" \--enable-
static \--disable-asm && \  
make -j4 && \  
make install && \  
# Install libfdk_aac  
cd /root/src && \  
git clone \--depth 1 https://github.com/mstorsjo/fdk-aac && \  
cd fdk-aac && \  
autoreconf -fiv && \  
./configure \--prefix="/root/soft/ffmpeg" \--disable-shared && \  
make -j4 && \  
make install && \  
# Install librtmp  
cd /root/src && \  
git clone git://git.ffmpeg.org/rtmpdump && \  
cd rtmpdump && \  
make -j4 && \  
make install && \  
\cp -rf /usr/local/lib/* /usr/lib64/ && \  
# Install ffmpeg  
cd /root/src/FFmpeg && \  
PATH="/root/soft/ffmpeg/bin:$PATH"
PKG_CONFIG_PATH="/root/soft/ffmpeg/lib/pkgconfig" ./configure \  
\--prefix="/root/soft/ffmpeg" \--pkg-config-flags="--static" \--extra-
cflags="-I /root/soft/ffmpeg/ffmpeg_build/include" \  
\--extra-ldflags="-L /root/soft/ffmpeg/lib" \--extra-libs=-lpthread \--extra-
libs=-lm \--bindir="/root/soft/ffmpeg/bin" \  
\--enable-gpl \--enable-libfdk_aac \--enable-libfreetype \--enable-libx264
\--enable-nonfree && \  
make -j4 && \  
make install && \  
ln -s /root/soft/ffmpeg/bin/ffmpeg /root/ffmpeg && \  
# Clean up the source  
rm -rf /root/src && \  
yum autoremove -y git wget autoconf automake make gcc kernel-headers patch cpp
nasm nasm* && \  
# Linking files  
ln -s /root/config/nginx.conf /root/soft/nginx/conf/nginx.conf && \  
#ln -s /root/config/nginx.conf /root/soft/senginx/conf/nginx.conf && \  
ln -s /root/shell/start_nginx.sh /root/start.sh && \  
ln -s /root/shell/stop.sh /root/stop.sh && \  
# Give permissions to files and folders  
chmod -R 777 /root/shell && \  
chmod -R 777 /root/web && \  
chmod -R 777 /root/logs && \  
chmod 777 /root  
# Volume settings  
VOLUME ["/root/logs","/root/web","/root/config"]  
# Port settings  
EXPOSE 80  
EXPOSE 1935  
# Startup Scripts  
CMD /bin/bash -c /root/start.sh

