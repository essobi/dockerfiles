FROM jenkins:alpine  
MAINTAINER scoutm33@ya.ru  
  
ARG user=jenkins  
  
USER root  
  
RUN echo "http://mirror.yandex.ru/mirrors/alpine/edge/community" >>
/etc/apk/repositories \  
&& apk --no-cache add docker \  
&& rm -rf /var/cache/apk/*  
  
USER ${user}  

