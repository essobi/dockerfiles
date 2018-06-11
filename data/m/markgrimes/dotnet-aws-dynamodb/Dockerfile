FROM microsoft/dotnet:sdk  
  
# Install zip which isn't part of the base image.  
RUN apt-get update -y \  
&& apt-get install -y zip  
  
# Install aws and all its dependencies  
RUN apt-get install -y git python-pip \  
&& pip install awscli  
  
# Install a Java runtime for DynamoDB  
RUN apt-get install -y default-jre  
# And download and unpack DynamoDB itself  
RUN mkdir /DynamoDB && \  
cd /DynamoDB && \  
curl -L https://s3-us-west-2.amazonaws.com/dynamodb-
local/dynamodb_local_latest.tar.gz | tar xz  

