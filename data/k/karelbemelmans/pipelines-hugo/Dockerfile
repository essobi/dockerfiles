FROM alpine:3.4  
MAINTAINER Karel Bemelmans <mail@karelbemelmans.com>  
  
# Install packages needed to build  
RUN apk add --update --no-cache \  
bash \  
ca-certificates \  
curl \  
python \  
py-pip \  
wget \  
&& pip install -U awscli  
  
# Install hugo.  
ARG HUGO_VERSION=0.17  
ARG
HUGO_SHA256=f1467e204cc469b9ca6f17c0dc4da4a620643b6d9a50cb7dce2508aaf8fbc1ea  
  
# Rember sha256sum (and md5sum) expect 2 spaces in front of the filename on
alpine...  
RUN curl -Ls
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz
\  
-o /tmp/hugo.tar.gz \  
&& echo "${HUGO_SHA256} /tmp/hugo.tar.gz" | sha256sum -c - \  
&& tar xf /tmp/hugo.tar.gz -C /tmp \  
&& mv /tmp/hugo_${HUGO_VERSION}_linux_amd64/hugo_${HUGO_VERSION}_linux_amd64
/usr/bin/hugo \  
&& rm -rf /tmp/hugo* \  

