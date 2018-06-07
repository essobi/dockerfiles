FROM atlassian/default-image:latest  
MAINTAINER "Jose Pacheco" <jose@icheko.com>  
  
# Install AWS CLI  
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip" && \  
unzip awscli-bundle.zip && \  
./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws  
  
# Install JSON processor  
RUN apt-get install jq

