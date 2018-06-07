FROM alpine:edge  
LABEL maintainer="Luis Elizondo"  
  
RUN apk update && apk add \  
build-base \  
libffi-dev \  
openssl-dev \  
python \  
python-dev \  
py-pip \  
zlib \  
bash \  
curl \  
less \  
jq \  
&& pip install --upgrade pip awscli \  
&& mkdir /root/.aws  
  
VOLUME /src  
WORKDIR /src  

