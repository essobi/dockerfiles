FROM python:3.6.3  
  
MAINTAINER Thomas Strohmeier  
  
RUN apt-get update && apt-get install -y jq software-properties-common \  
&& pip install awscli \  
&& curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-
cli-linux-amd64-latest \  
&& chmod +x /usr/local/bin/ecs-cli \  
&& add-apt-repository "deb http://ppa.launchpad.net/ansible/ansible/ubuntu
trusty main" \  
&& apt-key adv \--keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
\  
&& apt-get update && apt-get install -y ansible  

