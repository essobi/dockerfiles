FROM ubuntu:latest  
MAINTAINER david <david@cninone.com>  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && apt-get install -y letsencrypt lsof upstart-sysv \  
&& update-initramfs -u \  
&& apt-get purge systemd -y  
  
ENV TZ=Asia/Chongqing  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
ENTRYPOINT [ "letsencrypt" ]

