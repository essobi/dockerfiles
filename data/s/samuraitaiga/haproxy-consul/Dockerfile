FROM samuraitaiga/centos-consul  
MAINTAINER samuraitaiga  
  
WORKDIR /root  
  
ADD requirements.txt /root/  
RUN yum install -y haproxy python-devel python-setuptools gcc &&\  
easy_install pip &&\  
pip install -r requirements.txt  
  
ADD gen-haconfig /usr/local/bin/  
ADD refresh-hahosts.sh /usr/local/bin/  
ADD haproxy.cfg.j2 /root/  
  
RUN chmod +x /usr/local/bin/gen-haconfig && \  
chmod +x /usr/local/bin/refresh-hahosts.sh  

