FROM python:3.3-slim  
MAINTAINER Jared Short <jshort@trek10.com>  
  
RUN apt-get update && \  
apt-get install -y rename ssh && \  
pip install troposphere && \  
pip install awacs && \  
pip install boto3  
  
RUN mkdir /tmp/builder  
  
ADD ./deploy/* /tmp/builder/  
ADD ./iam/* /tmp/builder/  
  
# Make the related script executables  
RUN cd /tmp/builder && chmod -R +x . && rename 's/.py//' *.py && mv
/tmp/builder/* /usr/bin  
  
RUN mkdir /workspace && mkdir /root/.ssh  
  
WORKDIR /workspace  

