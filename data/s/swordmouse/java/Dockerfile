FROM java:8u111-jdk-alpine  
  
MAINTAINER Xi Liu <swordmouse@163.com>  
  
# change timezone  
ENV TZ=Asia/Shanghai  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \  
echo $TZ > /etc/timezone  
  
# Ensure UTF-8 locale  
ENV LANG zh_CN.UTF-8

