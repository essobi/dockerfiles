FROM debian:stable-slim  
  
VOLUME /config /media  
WORKDIR /app  
  
RUN apt-get update -y && apt-get install -q \--yes \--no-install-recommends \  
dumb-init apt-utils libc6 libc6-dev libglib2.0-0 libzip-dev\  
libjpeg62 libjpeg62-turbo-dev \  
zlib1g zlib1g-dev \  
wget build-essential autoconf automake libtool git \  
libavformat-dev libavcodec-dev libavutil-dev libav-tools libavdevice-dev
libswscale-dev \  
libsqlite3-dev \  
v4l-utils python-pip python-dev libssl-dev libcurl4-openssl-dev libjpeg-dev
ffmpeg \  
libjpeg-dev libwebp-dev \  
libzip-dev \  
x264 \  
python python-dev python-pip python-setuptools python-wheel \  
lsb-release pkg-config curl libcurl4-openssl-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -sL https://github.com/Motion-
Project/motion/archive/release-4.1.1.tar.gz | tar xz && \  
cd motion-release-4.1.1 && \  
autoreconf -fiv && \  
./configure \--with-webp && \  
make && \  
make install && \  
cd .. && \  
rm -rf motion-release-4.1.1  
  
RUN pip install motioneye  
  
RUN adduser \--no-create-home \--disabled-password \--gecos '' \--shell
/bin/false motion  
  
EXPOSE 8080 8081 8082 8765  
  
USER motion  
  
COPY upload /app  
  
CMD test -e /config/motion.conf || cp /usr/local/etc/motion/motion-dist.conf
/config/motion.conf && \  
test -e /config/motioneye.conf || cp
/usr/local/share/motioneye/extra/motioneye.conf.sample /config/motioneye.conf
&& \  
sed -i 's/\/etc\/motioneye/\/config/' /config/motioneye.conf && \  
sed -i 's/\/var\/run/\/config/' /config/motioneye.conf && \  
sed -i 's/\/var\/log/\/config/' /config/motioneye.conf && \  
sed -i 's/\/var\/lib\/motioneye/\/media/' /config/motioneye.conf && \  
sed -i 's/log_level debug/log_level info/' /config/motioneye.conf && \  
dumb-init meyectl startserver -c /config/motioneye.conf -d  
  
HEALTHCHECK CMD curl -f http://localhost:8765/ && \  
curl -s -f \--connect-timeout 5 \--head -o /dev/null http://localhost:8081 ||
exit 1  

