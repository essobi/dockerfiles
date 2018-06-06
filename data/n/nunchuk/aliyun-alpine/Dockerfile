############################################################  
# Dockerfile to build Alpine image for aliyun ecs  
# Based on Alpine:3.2  
############################################################  
  
FROM alpine:3.2  
MAINTAINER XinYe <nunchuk@live.com>  
  
# Add USTC repo  
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/'
/etc/apk/repositories \  
#  
# Set timezone  
&& apk add --update-cache tzdata \  
&& setup-timezone -z Asia/Shanghai \  
&& apk del tzdata \  
#cp /usr/share/zoneinfo/Europe/Brussels /etc/localtime  
#echo "Europe/Brussels" > /etc/timezone  
#  
# Sepcify ntp server  
&& sed -i 's/pool.ntp.org/cn.pool.ntp.org/' /etc/init.d/ntpd

