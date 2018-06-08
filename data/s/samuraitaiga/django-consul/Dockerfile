FROM samuraitaiga/centos-consul  
MAINTAINER samuraitaiga  
  
WORKDIR /root  
  
ADD requirements.txt /root/  
ADD jason_demo /root/jason_demo/  
ADD fire /usr/local/bin/  
RUN yum install -y python-setuptools && \  
easy_install pip && \  
pip install -r requirements.txt && \  
chmod +x /root/jason_demo/manage.py && \  
chmod +x /usr/local/bin/fire  
  
RUN yum install -y nmap  
ADD check-port /usr/local/bin/  
RUN chmod +x /usr/local/bin/check-port  
  
ADD django.json /root/  

