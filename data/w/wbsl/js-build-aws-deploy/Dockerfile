FROM node:6.10.0  
  
RUN apt-get update && apt-get install -y \  
python-dev \  
python-pip  
  
RUN pip install awscli  
  
RUN aws configure set preview.cloudfront true

