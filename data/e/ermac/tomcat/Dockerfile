# Dockerizing a base images with:  
#  
# \- Debian Stretch  
# \- Oracle JDK 8u131  
# \- Apache Tomcat 8.5.14  
# \- jRebel  
#  
# Build: docker build -t ermac/tomcat:8.5.14-jrebel .  
#  
# Run: docker run -ti ermac/tomcat:8.5.14-jrebel bash  
#  
# Example: docker run -it --rm ermac/tomcat:8.5.14-jrebel java -version  
# Example: docker run -p 8080:8080 -d ermac/tomcat:8.5.14-jrebel  
  
FROM ermac/tomcat:8.5.14  
  
MAINTAINER Fabio Martino <fabiomartino@libero.it>  
  
# Activate remote debug & JRebel agent  
ENV
JAVA_OPTS="-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5005
\  
-agentpath:/opt/jrebel/lib/libjrebel64.so -Drebel.remoting_plugin=true -Drebel.remoting_port=5555"  
  
# Get and install jRebel  
RUN (wget --progress=bar:force -O /tmp/jrebel.zip
http://dl.zeroturnaround.com/jrebel-stable-nosetup.zip &&\  
unzip -d /opt/ /tmp/jrebel.zip &&\  
rm /tmp/jrebel.zip)  
  
# Configuration  
#ADD myjar.jar /opt/tomcat/lib/  
#ADD logging.properties /opt/tomcat/conf/  
#ADD server.xml /opt/tomcat/conf/  
#ADD context.xml /opt/tomcat/conf/  
  
# JVM remote debug port  
EXPOSE 5005  
  
# JRebel remote agent port  
EXPOSE 5555  
  

