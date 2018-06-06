FROM python:2  
RUN apt-get update && apt-get install pkg-config python-dev build-essential
curl -y  
RUN pip install awscli  
RUN curl -sSL https://get.docker.com/ | sh  
RUN curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-
cli/ecs-cli-linux-amd64-latest && chmod +x /usr/local/bin/ecs-cli  

