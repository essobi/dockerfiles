FROM jenkins/jenkins:2.107.3  
ADD plugins.txt /  
RUN cat /plugins.txt | xargs /usr/local/bin/install-plugins.sh  

