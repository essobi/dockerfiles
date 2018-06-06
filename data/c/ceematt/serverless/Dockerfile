FROM drydock/u14:prod  
MAINTAINER Matt Snider (matt@cleanenergyexperts.com)  
  
# Updating Apt-get  
RUN mkdir -p /tmp && chmod 1777 /tmp  
RUN add-apt-repository -y ppa:chris-lea/node.js  
RUN add-apt-repository -y ppa:danmbox/ppa  
RUN apt-get -y update  
  
# Install NodeJS  
RUN apt-get -y install build-essential unzip  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -  
RUN apt-get -y install nodejs  
  
# Install Serverless  
RUN npm install serverless -g  
  
# Install AWS  
RUN cd /tmp && curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o
"awscli-bundle.zip" && unzip awscli-bundle.zip && ./awscli-bundle/install -i
/usr/local/aws -b /usr/local/bin/aws

