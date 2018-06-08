FROM node:6-alpine  
  
MAINTAINER LoyaltyOne  
  
# Default to UTF-8 file.encoding  
ENV LANG C.UTF-8  
# install curl, bash, kms-env 0.2.16 and s3-copy 0.0.2  
RUN apk upgrade --update && \  
apk add groff less python py-pip curl bash git openssl openssh && \  
pip install awscli && \  
apk --purge -v del py-pip && \  
rm /var/cache/apk/* && \  
npm install -g kms-env@0.2.16  
  
COPY env-decrypt s3-cp /usr/local/bin/  
ENTRYPOINT ["/usr/local/bin/env-decrypt"]  

