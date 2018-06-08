FROM alpine:latest  
LABEL maintainer="gie.spaepen@rombit.be"  
  
RUN apk update && apk add wget && apk add which && \  
cd /usr/local/bin && \  
wget
"https://github.com/gohugoio/hugo/releases/download/v0.32.4/hugo_0.32.4_Linux-32bit.tar.gz"
-O hugo.tar.gz && \  
tar -xvzf hugo.tar.gz hugo && rm hugo.tar.gz && \  
which hugo && \  
mkdir /build && \  
cd /build  
  
WORKDIR /build  
  
ENTRYPOINT pwd && hugo  
  

