FROM ranker/java  
  
MAINTAINER Vijay Mohan <vijay@ranker.com>  
  
RUN apt-get update  
  
# Install sshd  
RUN apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
  
# Set password to 'admin'  
RUN printf admin\\\nadmin\\\n | passwd  
  
# Install Tomcat 7  
RUN apt-get install -y tomcat7 tomcat7-admin  
RUN sed -i "s#</tomcat-users>##g" /etc/tomcat7/tomcat-users.xml; \  
echo ' <role rolename="manager-gui"/>' >> /etc/tomcat7/tomcat-users.xml; \  
echo ' <role rolename="manager-script"/>' >> /etc/tomcat7/tomcat-users.xml; \  
echo ' <role rolename="manager-jmx"/>' >> /etc/tomcat7/tomcat-users.xml; \  
echo ' <role rolename="manager-status"/>' >> /etc/tomcat7/tomcat-users.xml; \  
echo ' <role rolename="admin-gui"/>' >> /etc/tomcat7/tomcat-users.xml; \  
echo ' <role rolename="admin-script"/>' >> /etc/tomcat7/tomcat-users.xml; \  
echo ' <user username="admin" password="admin" roles="manager-gui, manager-
script, manager-jmx, manager-status, admin-gui, admin-script"/>' >>
/etc/tomcat7/tomcat-users.xml; \  
echo '</tomcat-users>' >> /etc/tomcat7/tomcat-users.xml  
  
EXPOSE 22  
EXPOSE 8080  
CMD service tomcat7 start; \  
/usr/sbin/sshd -D

