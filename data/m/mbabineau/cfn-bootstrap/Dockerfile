FROM debian:7.8  
  
MAINTAINER Mike Babineau <michael.babineau@gmail.com>  
  
RUN apt-get update \  
&& apt-get -y install --no-install-recommends \  
python=2.7.* \  
python-pip \  
  
&& pip install https://s3.amazonaws.com/cloudformation-examples/aws-cfn-
bootstrap-latest.tar.gz \  
  
&& apt-get -y purge python-pip \  
&& apt-get -y autoremove \  
&& apt-get autoclean \  
&& rm -rf /var/lib/apt/lists/*  

