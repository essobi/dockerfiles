FROM debian:wheezy  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# change original policy  
RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d  
  
# change source to local  
RUN cp /etc/apt/sources.list /etc/apt/sources.list.bak  
RUN printf 'deb http://mirrors.aliyun.com/debian wheezy main non-free contrib
\  
\ndeb http://mirrors.aliyun.com/debian wheezy-proposed-updates main contrib
non-free \  
\ndeb-src http://mirrors.aliyun.com/debian wheezy main non-free contrib \  
\ndeb-src http://mirrors.aliyun.com/debian wheezy-proposed-updates main
contrib non-free \  
\ndeb http://mirrors.aliyun.com/debian-security wheezy/updates main contrib
non-free \  
\ndeb-src http://mirrors.aliyun.com/debian-security wheezy/updates main
contrib non-free' > /etc/apt/sources.list  
  
# packages  
RUN apt-get update && apt-get install -y apt-utils \  
libreadline-dev \  
libpcre3-dev \  
libssl-dev \  
perl \  
curl \  
tar \  
make \  
gcc  
  
ENV OPEN_RESTY_VERSION 1.7.7.1  
# Fetch openresty and untar it  
RUN curl -sSL
http://openresty.org/download/ngx_openresty-${OPEN_RESTY_VERSION}.tar.gz \  
| tar -v -C /usr/src -xz  
  
# Build it and install it  
RUN cd /usr/src/ngx_openresty-${OPEN_RESTY_VERSION} && ./configure --with-
luajit && make && make install  
  
EXPOSE 80

