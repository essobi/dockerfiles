FROM python:2.7  
RUN mkdir -p /opt/rworker  
RUN mkdir -p /opt/rworker/log  
WORKDIR /opt/rworker  
ADD requirements.txt /opt/rworker/  
RUN apt-get update  
RUN apt-get install python-dev libldap2-dev libsasl2-dev libssl-dev -y  
RUN pip install -r /opt/rworker/requirements.txt  
  
CMD ["/bin/bash"]  

