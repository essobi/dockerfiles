FROM imix/java6  
  
COPY glassfish /opt/glassfish  
COPY commands.txt /opt/glassfish/commands.txt  
  
ENV JAVA_HOME="/usr/java/jdk1.6.0_45"  
ENV GLASSFISH_HOME="/opt/glassfish"  
# Set local time to Bogota  
RUN cp /usr/share/zoneinfo/America/Bogota /etc/localtime  
  
# For dev purpose install telnet  
#RUN yum install -y telnet  
WORKDIR /opt/glassfish  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod 777 /entrypoint.sh  
RUN chmod 777 /opt/glassfish/bin/asadmin  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
#CMD ["bin/asadmin", "multimode", "--file", "commands.txt"]  

