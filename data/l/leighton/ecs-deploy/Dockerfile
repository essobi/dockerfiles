FROM docker:latest  
  
MAINTAINER Mo Gusbi <mo.gusbi@leighton.com>  
  
COPY tools/ecs-check /usr/local/bin/  
  
RUN apk add --update bash curl python py-pip  
  
RUN curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-
cli/ecs-cli-linux-amd64-latest  
  
RUN chmod +x /usr/local/bin/ecs-check  
  
RUN chmod +x /usr/local/bin/ecs-cli  

