FROM jenkins:latest  
USER root  
RUN mkdir /var/lib/jenkins && chmod 777 -R /var/lib/jenkins  
ENV JENKINS_HOME /var/lib/jenkins  
ENV COPY_REFERENCE_FILE_LOG /var/lib/jenkins/copy_reference_file.log  
USER jenkins  

