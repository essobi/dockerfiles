FROM centos:7  
RUN \  
yum install -y epel-release && \  
yum install -y git python-pip && \  
pip install flask  
  
COPY aat /aat  
  
WORKDIR aat  
  
EXPOSE 5000  
CMD python aat.py  

