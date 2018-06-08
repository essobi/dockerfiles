FROM octasic/base_jenkins_slave  
  
LABEL Description="Jenkins slave meant for running python3 test suites"  
  
USER root  
  
RUN apt-get -y update && \  
apt-get install -y gdb python3 python-pip && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN pip install unittest-xml-reporting  
  
USER jenkins  

