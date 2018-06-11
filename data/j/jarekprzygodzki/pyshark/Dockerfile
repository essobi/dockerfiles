FROM centos  
  
MAINTAINER Jarek Przygódzki <jarek.przygodzki@gmail.com>  
RUN  yum -y update && \  
yum -y install epel-release && \  
yum -y install python34 \  
yum -y install wireshark && yum clean all && \  
curl -O https://bootstrap.pypa.io/get-pip.py && \  
/usr/bin/python3.4 get-pip.py && \  
rm get-pip.py && \  
pip install pyshark && \  
pip install tqdm requests  
  
CMD ["python3"]  

