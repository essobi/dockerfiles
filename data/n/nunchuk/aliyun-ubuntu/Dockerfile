############################################################  
# Dockerfile to build Ubuntu image for aliyun ecs  
# Based on Ubuntu:14.04  
############################################################  
  
FROM ubuntu:14.04  
MAINTAINER XinYe <nunchuk@live.com>  
  
# Replace by aliyun repository URL instead the default sources  
RUN sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/' /etc/apt/sources.list  
  
# Update the repository and patch system  
RUN apt-get update -y && \  
apt-get install bash libc6 libc-bin openssl wget ntp -y  
  
# delete all the apt list files since they're big and get stale quickly  
RUN rm -rf /var/lib/apt/lists/*  
  
# Replace by aliyun ntp server  
ADD ntp.conf /etc/ntp.conf  
  
# change default time zone  
# ls -R --group-directories-first /usr/share/zoneinfo  
RUN rm /etc/localtime && ln -sf /usr/share/zoneinfo/Asia/Shanghai
/etc/localtime  
  
# change dns server  
RUN echo 'nameserver 223.5.5.5' >> /etc/resolvconf/resolv.conf.d/tail &&
resolvconf -u

