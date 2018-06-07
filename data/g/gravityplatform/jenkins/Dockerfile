FROM jenkins  
  
COPY plugins.txt /usr/share/jenkins/plugins.txt  
#download error with version URL and added curl retry  
COPY plugins.retry.sh /usr/local/bin/plugins.sh  
  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  

