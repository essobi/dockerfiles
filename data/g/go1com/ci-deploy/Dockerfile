FROM node:alpine  
  
RUN \  
mkdir -p /aws && \  
apk -Uuv add curl docker git groff jq less python py-pip && \  
pip install awscli && \  
curl -o /usr/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-
linux-amd64-latest && \  
chmod a+x /usr/bin/ecs-cli && \  
npm install -g semver && \  
apk --purge -v del py-pip && \  
rm /var/cache/apk/*  

