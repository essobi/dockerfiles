FROM debian:latest  
MAINTAINER Gustavo Lichti <gustavo.lichti@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
zip \  
unzip \  
curl \  
python \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV LANG C.UTF-8  
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "/awscli-
bundle.zip"  
RUN unzip /awscli-bundle.zip  
RUN /awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws  
  
RUN mkdir -p /root/.aws  
  

