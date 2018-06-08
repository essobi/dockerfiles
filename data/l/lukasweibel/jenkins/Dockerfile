FROM jenkins  
COPY plugins.txt /usr/share/jenkins/ref/  
COPY custom.groovy /usr/share/jenkins/ref/init.groovy  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/ref/plugins.txt  

