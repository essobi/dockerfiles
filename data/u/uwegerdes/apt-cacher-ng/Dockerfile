# apt-cacher-ng docker image for use with my baseimage  
FROM ubuntu:latest  
MAINTAINER entwicklung@uwegerdes.de  
  
ARG TZ=UTC  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TZ ${TZ}  
  
RUN echo '${TZ}' >/etc/timezone && \  
apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get install -y \  
apt-cacher-ng && \  
rm -rf /var/lib/apt/lists/* && \  
sed -i -e 's/# Port:3142/Port:3142/g' /etc/apt-cacher-ng/acng.conf && \  
sed -i -e 's/# ForeGround: 0/ForeGround: 1/g' /etc/apt-cacher-ng/acng.conf &&
\  
sed -i -e 's/LogDir: \/var\/log\/apt-cacher-ng/LogDir: \/var\/cache\/apt-
cacher-ng/g' /etc/apt-cacher-ng/acng.conf  
  
VOLUME "/var/cache/apt-cacher-ng"  
  
EXPOSE 3142  
CMD /usr/sbin/apt-cacher-ng -c /etc/apt-cacher-ng  
  

