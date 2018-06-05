FROM debian  
  
RUN apt-get update && apt-get install -y git python python-dev python-pip  
RUN apt-get install -y build-essential libev4 libev-dev  
RUN pip install setuptools --upgrade  
RUN pip install six --upgrade  
RUN pip install cassandra-driver  
RUN echo "install code 22"  
RUN cd /root && git clone https://github.com/osallou/sysdig-analyser.git  
RUN cd /root/sysdig-analyser && python setup.py install  
RUN cp /root/sysdig-analyser/config.yml.example /root/sysdig-
analyser/config.yml  
  
WORKDIR /root/sysdig-analyser  
RUN mkdir -p /opt/prometheus-multiproc  
ENV prometheus_multiproc_dir=/opt/prometheus-multiproc  

