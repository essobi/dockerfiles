FROM java:latest  
MAINTAINER Udo Meijer (udo.meijer@gmail.com)  
  
RUN wget -O /tmp/AuditConsole-0.4.6-13-standalone.zip
https://download.jwall.org/AuditConsole/current/AuditConsole-0.4.6-13-standalone.zip
\  
&& unzip /tmp/AuditConsole-0.4.6-13-standalone.zip -d /opt \  
&& rm -f /tmp/AuditConsole-0.4.6-13-standalone.zip \  
&& chmod 755 /opt/AuditConsole/bin/*.sh  
  
EXPOSE 8080  
  
CMD ["/opt/AuditConsole/bin/catalina.sh", "run"]  

