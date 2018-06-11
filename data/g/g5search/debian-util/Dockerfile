FROM debian:jessie  
  
RUN apt-get update && \  
apt-get install -y openssh-client git vim zip curl python ruby jq  
  
WORKDIR /  
  
# install aws cli  
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip"  
RUN unzip awscli-bundle.zip  
RUN ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws  
  
# This ruby client will be used for pushing metrics to prometheus  
RUN gem install --no-doc prometheus-client  

