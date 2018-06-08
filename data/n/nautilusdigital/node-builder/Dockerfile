FROM node:10.0.0-alpine  
  
# Install development packages  
RUN apk add --no-cache --update bash curl git openssh docker jq make && \  
rm -rf /var/cache/apk/*  
  
# Install AWS CLI  
RUN apk --no-cache update && \  
apk --no-cache add python py-pip py-setuptools ca-certificates groff less && \  
pip --no-cache-dir install awscli && \  
rm -rf /var/cache/apk/*  
  
# Install Docker Compose  
RUN pip --no-cache-dir install docker-compose && \  
rm -rf /var/cache/apk/*  
  
# Install ECS Deploy  
RUN curl https://raw.githubusercontent.com/silinternational/ecs-
deploy/master/ecs-deploy | tee -a /usr/bin/ecs-deploy && \  
chmod +x /usr/bin/ecs-deploy  
  
# Install Node.js packages  
RUN yarn global add \  
conventional-github-releaser \  
bunyan  
  
RUN yarn config set ignore-engines true  

