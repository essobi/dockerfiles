FROM python:3.6-stretch  
  
# for AWS Cli tools  
RUN pip install --upgrade pip awscli boto3  
  
# for Angular applications  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs  
  
# install rsync for deployments  
RUN apt-get install -y rsync  

