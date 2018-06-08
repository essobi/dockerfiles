FROM alpine:3.6  
MAINTAINER Arek Czogala <aczogala@gmail.com>  
  
ADD config.env /config.env  
  
RUN source /config.env && \  
apk --no-cache update && \  
apk add python py-pip curl sudo jq=$JQ_VERSION tar groff less bash  
  
RUN source /config.env && \  
pip install --upgrade pip && \  
pip install awscli==$AWS_CLI_VERSION awsebcli==$AWS_EB_CLI  
  
RUN source /config.env && \  
curl -sL https://github.com/silinternational/ecs-
deploy/archive/$ECS_DEPLOY_VERSION.tar.gz | tar -xzv && \  
ln -s /ecs-deploy-$ECS_DEPLOY_VERSION/ecs-deploy /usr/bin/ecs-deploy  

