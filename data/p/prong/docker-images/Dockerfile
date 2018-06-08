FROM openjdk:8-jdk-alpine  
  
MAINTAINER visionken <visionken2017@qq.com>  
  
# 基于alpine的镜像时区修改为中国  
RUN apk --no-cache add tzdata && \  
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \  
echo "Asia/Shanghai" > /etc/timezone  
  
ENV JAVA_OPTS=""  
VOLUME /tmp  
  
# Install curl and bash for the entry script  
RUN apk --update add curl bash && \  
rm -rf /var/cache/apk/*  

