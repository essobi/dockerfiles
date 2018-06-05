FROM jenkins/jenkins  
  
USER root  
  
RUN apt-get update && apt-get install -y python-pip && rm -rf
/var/lib/apt/lists/*  
RUN pip install ansible  
  
USER jenkins  

