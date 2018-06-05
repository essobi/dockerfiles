# base image  
FROM alpine:3.6  
MAINTAINER LancnHan <larcnhan@126.com>  
  
ARG TIME_ZONE=Asia/Shanghai  
ENV TIME_ZONE ${TIME_ZONE}  
RUN apk add --no-cache tzdata \  
&& echo "${TIME_ZONE}" > /etc/timezone \  
&& ln -sf /usr/share/zoneinfo/${TIME_ZONE} /etc/localtime  
  
CMD ["/bin/sh"]  

