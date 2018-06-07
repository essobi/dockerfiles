FROM alpine:edge  
MAINTAINER Xueshan Feng <sfeng@stanford.edu> & Chris Hunter  
  
ENV AWSCLI_VERSION "1.14.51"  
RUN apk update && apk add \  
bash \  
curl \  
less \  
groff \  
jq \  
python \  
py-pip \  
py2-pip && \  
pip install \--upgrade pip awscli==${AWSCLI_VERSION} s3cmd && \  
mkdir /root/.aws  
  
COPY get-metadata /usr/local/bin/get-metadata  
# Expose data volume  
VOLUME /apps  

