FROM maven:3.5.3-jdk-8  
  
LABEL authors="Saurabh Oza, Jonas Tepe"  
  
WORKDIR /root/  
  
RUN apt-get update \  
&& apt-get install -y lsb-release sudo software-properties-common apt-
transport-https python-pip \  
&& pip install docker-compose \  
&& pip install awscli \--upgrade --user \  
&& pip install boto3 \  
&& curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add
\- \  
&& add-apt-repository "deb [arch=amd64]
https://download.docker.com/linux/debian $(lsb_release -cs) stable" \  
&& apt-get update \  
&& apt-get install -y docker-ce  

