FROM debian:jessie  
  
MAINTAINER Wang Sigeng "wangsigeng2012@gmail.com"  
ENV LANG C.UTF-8  
ENV TZ=Asia/Shanghai  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
RUN apt-get update \  
&& apt-get install -y --force-yes --no-install-recommends \  
libc6-i386 \  
lib32z1 \  
zlib1g\  
&& apt-get autoclean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /xware  
ADD Xware1.0.31_x86_32_glibc.tar.gz /xware  
ADD docker-entrypoint.sh /xware  
VOLUME /data  
  
CMD ["./docker-entrypoint.sh"]

