FROM ubuntu:trusty  
  
MAINTAINER jrudolph  
  
RUN apt-get update  
  
RUN apt-get install -y python-dev libffi-dev libssl-dev && \  
apt-get install -y python-setuptools && \  
easy_install unittest2 && \  
easy_install pyasn1 && \  
easy_install autobahntestsuite && \  
apt-get install -y python libssl1.0.0 libffi6 && \  
apt-get remove -y libffi-dev libssl-dev && \  
apt-get autoremove -y && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
EXPOSE 8080 9001  
WORKDIR /tmp  
  
CMD wstest -m fuzzingserver  

