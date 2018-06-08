FROM centos:7  
RUN yum install -y epel-release && \  
yum install -y python-setuptools python-pip && \  
pip install virtualenv  
  
RUN mkdir -p /app && \  
cd /app && virtualenv venv && \  
source venv/bin/activate && \  
pip install rollbar-agent && \  
chmod +x /app/venv/rollbar-agent  
  
COPY ./rollbar-agent.conf /app/venv/rollbar-agent.conf  
  
COPY ./run.py /app/venv/run.py  
  
WORKDIR /app/venv/  
  
CMD source bin/activate && python ./run.py

