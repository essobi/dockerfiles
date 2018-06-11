FROM alpine:latest  
  
RUN apk add --no-cache python ca-certificates py2-certifi openssh-client
sshpass  
RUN apk add --no-cache --virtual build-dependencies python-dev py-pip gcc
musl-dev libffi-dev openssl-dev make \  
&& pip install --upgrade pip \  
&& pip install ansible \  
&& apk del build-dependencies \  
&& rm -r ~/.cache/pip  
  
WORKDIR /infra  

