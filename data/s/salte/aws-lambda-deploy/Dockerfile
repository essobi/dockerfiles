FROM ubuntu:16.04  
MAINTAINER Dave Woodward <dave@salte.io>  
  
RUN apt-get update && \  
apt-get install -y zip && \  
apt-get install -y python-pip && \  
apt-get install -y python-software-properties && \  
apt-get install -y curl && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y nodejs && \  
apt-get install -y jq && \  
apt-get install -y groff && \  
apt-get install -y git && \  
apt-get clean  
  
RUN pip install --upgrade pip && \  
pip install awscli && \  
pip install --upgrade awsebcli  
  
CMD ["aws"]  

