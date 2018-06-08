FROM goldeneggg/centos-python27  
  
MAINTAINER goldeneggg  
  
RUN yum -y install libevent libevent-devel  
  
WORKDIR /root  
RUN git clone https://github.com/progrium/requestbin.git  
WORKDIR /root/requestbin  
RUN pip install -r requirements.txt  
RUN python setup.py install  
  
ENV PORT 5550  
ENTRYPOINT ["python", "web.py"]  

