FROM alpine:3.4  
MAINTAINER Avi Miller <avi.miller@gmail.com>  
  
ENV HUGO_VERSION=0.18.1 \  
HUGO_MD5SUM=e8ba723c508e87912970f132534c64dc  
  
RUN set -ex && \  
apk add --no-cache openssl openssh-client git py-pygments  
  
RUN wget -q
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz
&& \  
echo "${HUGO_MD5SUM} hugo_${HUGO_VERSION}_Linux-64bit.tar.gz" | md5sum -c && \  
tar xf hugo_${HUGO_VERSION}_Linux-64bit.tar.gz && \  
cp hugo_${HUGO_VERSION}_linux_amd64/hugo_${HUGO_VERSION}_linux_amd64
/usr/bin/hugo && \  
rm -rf hugo_${HUGO_VERSION}_linux_amd64 && \  
rm -f hugo_${HUGO_VERSION}_linux_amd64.tar.gz  
  
CMD ["hugo"]  

