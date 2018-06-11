FROM ruby:2.3.2  
  
#Dependencies  
RUN apt-get update && \  
apt-get install -y build-essential python-dev ruby-full zip \--no-install-
recommends && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#Pip  
RUN \  
curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
pip install \--upgrade awsebcli awscli boto3==1.3.0 && \  
aws configure set preview.cloudfront true && \  
rm -rf get-pip.py  
ENTRYPOINT ["/bin/bash"]

