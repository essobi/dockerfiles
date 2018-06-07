FROM jenkins/jnlp-slave  
  
USER root  
  
RUN apt-get update && apt-get -y install libltdl7 python-pip  
RUN pip install ansible jmespath  
  
USER jenkins  

