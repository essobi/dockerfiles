FROM python:2  
# migration to pypy ?  
WORKDIR /root/  
RUN apt update && apt install -y python-setuptools fuse  
  
RUN git clone https://github.com/remakeelectric/mqtt-malaria.git  
WORKDIR /root/mqtt-malaria  
  
RUN python setup.py build  
RUN python setup.py install  

