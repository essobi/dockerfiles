FROM ubuntu:14.04  
#Install universal packages used in all repositories  
RUN apt-get update && apt-get install -y \  
build-essential \  
g++ \  
gcc \  
make \  
python \  
python-dev \  
python-pip \  
u-boot-tools \  
wget \  
&& apt-get clean  
  
RUN pip install --upgrade pip \  
&& pip install --upgrade virtualenv \  
&& pip install awscli \  
&& pip install boto3  

