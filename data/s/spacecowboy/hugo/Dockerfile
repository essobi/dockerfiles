FROM alpine:latest  
MAINTAINER Jonas Kalderstam, jonas@cowboyprogrammer.org  
  
RUN apk --update add ca-certificates py-pygments py-setuptools wget && rm -rf
/var/cache/apk/*  
  
ENV HUGO_VER 0.15  
RUN wget
https://github.com/spf13/hugo/releases/download/v${HUGO_VER}/hugo_${HUGO_VER}_linux_amd64.tar.gz
&& \  
tar zxvf hugo_${HUGO_VER}_linux_amd64.tar.gz && \  
cd hugo_${HUGO_VER}_linux_amd64 && \  
mv hugo_${HUGO_VER}_linux_amd64 /usr/local/bin/hugo && \  
cd / && \  
rm -rf hugo_${HUGO_VER}_linux_amd64 && \  
chmod +x /usr/local/bin/hugo && \  
mkdir /data  
  
WORKDIR /data  
  
ENTRYPOINT ["/usr/local/bin/hugo"]  

