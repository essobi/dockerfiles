FROM openjdk:8-jdk-alpine  
  
LABEL maintainer="Ramiro Rivera <ramarivera@gmail.com>"  
  
RUN apk add --update \  
curl \  
ca-certificates \  
bash \  
coreutils \  
jq \  
unzip \  
wget \  
gnupg  
  
RUN apk add --no-cache python3 && \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools && \  
if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \  
if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python;
fi && \  
rm -r /root/.cache  

