FROM jenkins/jenkins:alpine  
LABEL maintainer="Tao Wang <moonavw@gmail.com>"  
  
USER root  
  
# https://wiki.alpinelinux.org/wiki/Docker  
# use mirror since dl-cdn.alpinelinux.org is unstable  
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/community" >
/etc/apk/repositories \  
&& echo "http://dl-4.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories \  
&& apk add \--update docker  
  
RUN apk add \--update py-pip \  
&& pip install docker-compose  
  
RUN apk add \--update shadow \  
&& groupadd -g 50 staff \  
&& usermod -a -G staff jenkins  
  
USER jenkins  

