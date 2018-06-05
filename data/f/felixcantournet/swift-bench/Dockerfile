# COPYRIGHT (c) 2015 Cloudwatt  
FROM python:2  
MAINTAINER Félix Cantournet "felix.cantournet@cloudwatt.com"  
RUN mkdir /tempo && git clone https://github.com/openstack/swift-bench.git
/tempo  
WORKDIR /tempo  
RUN pip install -r requirements.txt  
RUN pip install python-keystoneclient  
RUN python setup.py install  
  
ENTRYPOINT ["swift-bench", "/etc/swift/sbench.conf"]  

