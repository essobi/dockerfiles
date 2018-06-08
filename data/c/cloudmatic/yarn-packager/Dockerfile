FROM alpine:edge  
MAINTAINER Mauricio Araya  
  
ENV LANGUAGE=en_US  
ENV LANG=en_US.UTF-8  
  
RUN apk upgrade \--update  
  
COPY pack-n-upload.sh /usr/local/bin/pack-n-upload.sh  
  
RUN chmod 755 /usr/local/bin/pack-n-upload.sh  
  
RUN apk add \--no-cache --update jq build-base alpine-sdk bash zip python3
python3-dev nodejs nodejs-npm && \  
python3 -m ensurepip && \  
pip3 install --upgrade pip setuptools awscli && \  
if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \  
if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python;
fi && \  
npm install -g yarn && \  
rm -rf /root/.cache && apk del build-base alpine-sdk  

