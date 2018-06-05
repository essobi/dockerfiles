FROM google/debian:wheezy  
  
ADD openmrs-runtime.properties /var/lib/tomcat7/openmrs-runtime.properties  
ADD run.sh /root/run.sh  
  
RUN apt-get update; \  
apt-get install -y curl openjdk-7-jre tomcat7; \  
curl -L
http://sourceforge.net/projects/openmrs/files/releases/OpenMRS_Platform_1.10.1/openmrs.war/download
\  
-o /var/lib/tomcat7/webapps/openmrs.war; \  
apt-get install -y mysql-server; \  
mkdir /var/lib/OpenMRS; \  
chown tomcat7:tomcat7 /var/lib/tomcat7/openmrs-runtime.properties
/var/lib/OpenMRS; \  
chmod +x /root/run.sh  
  
EXPOSE 8080  
  
CMD ["/root/run.sh"]  

