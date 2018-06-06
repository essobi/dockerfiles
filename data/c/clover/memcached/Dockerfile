FROM library/ubuntu:bionic AS build  
  
ENV LANG=C.UTF-8  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y \  
software-properties-common \  
apt-utils  
  
RUN mkdir -p /build /rootfs  
WORKDIR /build  
RUN apt-get download \  
memcached \  
libevent-2.1-6 \  
libsasl2-2 \  
libsasl2-modules-db \  
libdb5.3  
RUN find *.deb | xargs -I % dpkg-deb -x % /rootfs  
  
WORKDIR /rootfs  
RUN rm -rf \  
etc \  
lib \  
usr/include \  
usr/share  
  
WORKDIR /  
  
FROM clover/base  
  
ENV LANG=C.UTF-8  
COPY \--from=build /rootfs /  
  
CMD ["memcached", "-u", "root", "-v", "-m", "64", "-c", "1024", "-t", "4",
"-I", "1m", "-b", "1024", "-R", "20"]  
  
EXPOSE 11211  

