FROM alpine:latest  
MAINTAINER kebyn <kebyn@sina.com>  
ENV LANG C.UTF-8  
ENV TZ Asia/Shanghai  
  
RUN set -ex \  
&& apk add \--no-cache python curl \  
&& apk add \--no-cache \--virtual .deps \  
git \  
&& curl -L -s -o get-pip.py https://bootstrap.pypa.io/get-pip.py \  
&& python get-pip.py \  
&& rm get-pip.py \  
&& pip install git+https://github.com/shadowsocks/shadowsocks.git@master \  
&& apk del .deps  
  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  

