FROM alpine:3.6  
MAINTAINER limed@sudoers.org  
  
RUN apk --no-cache add bash \  
bash-completion \  
ca-certificates \  
python \  
py-pip \  
&& rm -rf /var/cache/apk/*  
  
RUN mkdir -p /data \  
/config \  
/app  

