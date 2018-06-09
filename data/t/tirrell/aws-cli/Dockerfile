  
FROM alpine:edge  
MAINTAINER Guilherme Oliveira <gwoliveira@gmail.com>  
  
RUN apk update && apk add \  
bash \  
curl \  
less \  
groff \  
jq \  
python \  
py-pip \  
py2-pip && \  
pip install --upgrade pip awscli s3cmd && \  
mkdir /root/.aws  

