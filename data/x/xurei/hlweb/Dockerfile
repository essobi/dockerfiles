FROM node:8.9.0-alpine  
  
RUN apk update && \  
apk add --no-cache bash curl git openssh groff less python py-pip zip && \  
pip install awscli && \  
apk --purge -v del py-pip && \  
rm /var/cache/apk/*  
  
RUN git clone https://github.com/s3tools/s3cmd.git /opt/s3cmd && \  
ln -s /opt/s3cmd/s3cmd /usr/bin/s3cmd  
  
WORKDIR /cache  
  
# use changes to package.json to force Docker not to use the cache  
# when we change our application's nodejs dependencies:  
ADD package.json /cache/package.json  
ADD package-lock.json /cache/package-lock.json  
RUN npm install --no-progress && npm cache clear --force  
  
USER root  
  
RUN git config --global user.email "bot@hackleague.io" && git config --global
user.name "hlbot"  
  

