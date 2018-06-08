FROM zabbix/zabbix-server-mysql:alpine-latest  
MAINTAINER comphilip@msn.com  
RUN echo 'http://dl-cdn.alpinelinux.org/alpine/edge/community' >>
/etc/apk/repositories \  
&& echo 'http://dl-cdn.alpinelinux.org/alpine/edge/main' >>
/etc/apk/repositories \  
&& apk add \--no-cache python3 curl \  
&& curl -Lo get-pip.py https://bootstrap.pypa.io/get-pip.py \  
&& python3 get-pip.py \  
&& rm get-pip.py \  
&& pip install virtualenv  

