FROM openjdk:7  
MAINTAINER Arturo Volpe <arturovolpe@gmail.com>  
RUN useradd -m -d /opt/jboss -s /bin/bash jboss  
USER jboss  
  
ENV JBOSS_VERSION 4.0.5.GA  
RUN cd $home && wget
http://sourceforge.net/projects/jboss/files/JBoss/JBoss-$JBOSS_VERSION/jboss-$JBOSS_VERSION.zip
&& unzip jboss-$JBOSS_VERSION.zip && rm jboss-$JBOSS_VERSION.zip  
  
# Enable remote debugging  
ENV
JAVA_OPTS=-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=8000  
# Expose the ports we're interested in  
# Webserver is running on 8080  
# Adminserver is running on 9990  
# Remote debug port can be accessed on 8000  
EXPOSE 8080 9990 8000 1098 1099 3873 4444 4445 4446 8009 8083 8090 8092 8093  
# Configurations  
ENV JBOSS_HOME=/opt/jboss/jboss-$JBOSS_VERSION  
  
ADD run.sh /opt/run.sh  
# Set the default command to run on boot  
CMD ["/bin/bash", "/opt/run.sh"]  

