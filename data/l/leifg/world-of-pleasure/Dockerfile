FROM ruby:2.5.0  
LABEL maintainer="Leif Gensert <leif@leif.io>"  
  
RUN apt-get update  
RUN apt-get -y install python2.7-minimal python2.7-dev zip unzip  
  
# Install AWS CLI  
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip"  
RUN unzip awscli-bundle.zip  
RUN ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws  
RUN rm -rf ./awscli-bundle/  

