############################################################  
# Dockerfile to build Debian image for aliyun ecs  
# Based on Debian:8(jessie)  
############################################################  
  
FROM debian:8  
MAINTAINER XinYe <nunchuk@live.com>  
  
# Replace by aliyun repository URL instead the default sources  
#wget -qO /etc/apt/sources.list
http://mirrors.aliyun.com/repo/debian8-lts.list  
COPY debian8-lts.list /etc/apt/sources.list  
  
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
RUN echo 'nameserver 223.5.5.5' >> /etc/resolv.conf

