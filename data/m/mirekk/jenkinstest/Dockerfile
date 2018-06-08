FROM jboss/wildfly:8.2.1.Final  
  
USER root  
  
RUN /opt/jboss/wildfly/bin/add-user.sh admin admin --silent  
  
# JENKINS  
RUN curl -L -o /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat-
stable/jenkins.repo  
RUN rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key  
RUN yum -y install jenkins  
RUN chkconfig jenkins on  
  
RUN chown -R jenkins:0 /var/log/jenkins  
RUN chown -R jenkins:0 /var/lib/jenkins  
RUN chown -R jenkins:0 /var/cache/jenkins  
  
EXPOSE 8080  
EXPOSE 50000  
CMD ["/bin/bash"]  

