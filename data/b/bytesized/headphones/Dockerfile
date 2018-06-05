FROM bytesized/base  
MAINTAINER maran@bytesized-hosting.com  
  
RUN apk add \--no-cache ffmpeg  
  
RUN apk add \--no-cache \--virtual=build-dependencies g++ gcc make git python
&& \  
mkdir -p \  
/tmp/shntool && \  
curl -o \  
/tmp/shntool-src-tar.gz -L \  
http://www.etree.org/shnutils/shntool/dist/src/shntool-3.0.10.tar.gz && \  
tar xf /tmp/shntool-src-tar.gz -C \  
/tmp/shntool \--strip-components=1 && \  
cd /tmp/shntool && \  
./configure \  
\--infodir=/usr/share/info \  
\--localstatedir=/var \  
\--mandir=/usr/share/man \  
\--prefix=/usr \  
\--sysconfdir=/etc && \  
make && \  
make install && \  
  
apk del \--purge g++ gcc make && \  
rm -rf \  
/tmp/* \  
/usr/lib/*.la && cd && mkdir -p /app/ && \  
git clone https://github.com/rembo10/headphones.git \--depth 2 /app/headphones  
  
COPY static/ /  
  
EXPOSE 8181  
  
VOLUME /config /data /media  

