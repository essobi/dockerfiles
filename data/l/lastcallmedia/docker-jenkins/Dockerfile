FROM jenkins:2.60.2  
  
USER root  
RUN apt-get update && apt-get install -y libltdl7 rsync jq && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
USER jenkins

