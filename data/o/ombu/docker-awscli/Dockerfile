FROM alpine:latest  
  
LABEL maintainer=OMBU  
  
WORKDIR /tmp  
  
RUN \  
apk -Uuv add --no-cache groff less python py-pip curl && \  
pip install awscli awslogs && \  
curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-
cli-linux-amd64-latest && \  
chmod +x /usr/local/bin/ecs-cli && \  
rm -rf /var/cache/apk/*  

