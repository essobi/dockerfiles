FROM alpine:3.7  
MAINTAINER towb <me@towb.xyz>  
  
RUN set -x \  
&& apk add --no-cache \  
ca-certificates \  
py2-pip \  
&& pip install --upgrade pip \  
&& pip install setuptools \  
&& pip install flexget \  
&& mkdir /flexget  
  
ENV LOGLEVEL info  
  
CMD flexget --loglevel $LOGLEVEL -c /flexget/config.yml daemon start  

