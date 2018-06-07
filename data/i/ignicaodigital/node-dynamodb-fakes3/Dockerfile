FROM ignicaodigital/node-dynamodb  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN \  
apt-get update && \  
apt-get install -y ruby build-essential python-dev && \  
gem install fakes3 && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN \  
curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
pip install \--upgrade awscli boto3==1.3.0 && \  
rm -rf get-pip.py  
EXPOSE 4567  
  
ENTRYPOINT ["fakes3", "-r", "/mnt/fakes3_root", "-H", "s3.local", "-p",
"4567"]  

