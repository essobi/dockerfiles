FROM alpine:3.7  
  
ENV AWS_CLI_VERSION=1.15.28  
  
RUN apk -v --update add \  
python \  
py-pip \  
ca-certificates \  
curl \  
git \  
gzip \  
zip \  
tar \  
jq \  
&& \  
pip install --upgrade awscli==${AWS_CLI_VERSION} s3cmd==2.0.1 && \  
apk -v --purge del py-pip && \  
rm /var/cache/apk/*  

