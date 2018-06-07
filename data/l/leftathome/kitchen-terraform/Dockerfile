FROM chef/chefdk:latest  
MAINTAINER leftathome@gmail.com  
ENTRYPOINT "/bin/sh"  
ARG TF_VERSION=0.11.5  
WORKDIR /tmp  
ADD Gemfile .  
RUN apt-get update && apt-get install -y unzip \  
git build-essential && apt-get clean && \  
chef exec bundle install && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN wget
https://releases.hashicorp.com/terraform/${TF_VERSION}/terraform_${TF_VERSION}_linux_amd64.zip
&& unzip terraform_${TF_VERSION}_linux_amd64.zip -d /usr/bin/ && rm
terraform_*.zip  
ENTRYPOINT /bin/bash  

