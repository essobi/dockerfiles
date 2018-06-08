FROM ubuntu  
RUN groupdel www-data || true  
RUN userdel www-data || true  
RUN groupadd tomcat6 -g 8080  
RUN useradd tomcat6 -u 8080 -g 8080 -M -d /usr/share/tomcat6 -s /bin/false  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install tomcat6  
RUN /bin/echo -e "CATALINA_BASE=/var/lib/tomcat6\n\  
CATALINA_HOME=/usr/share/tomcat6\n\  
CATALINA_TMPDIR=/tmp/tomcat6-tomcat6-tmp" >> /usr/share/tomcat6/bin/setenv.sh  
ADD . /opt/nicedocker  
ADD crontab /etc/crontab  
EXPOSE 8080  
CMD ["/opt/nicedocker/run.sh"]  

