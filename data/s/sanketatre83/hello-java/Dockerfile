#  
# Oracle Java 8 Dockerfile  
#  
# https://github.com/dockerfile/java  
# https://github.com/dockerfile/java/tree/master/oracle-java8  
#  
# Pull base image.  
FROM ubuntu:16.04  
# Install Java.  
RUN apt-get update  
RUN apt-get install -y software-properties-common  
# Install Java.  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer && \  
apt-get update && \  
apt-get install -y maven && \  
apt-get install -y vim && \  
apt-get install -y tomcat8 && \  
apt-get install -y net-tools && \  
echo "JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> /etc/default/tomcat8  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
# Define working directory.  
WORKDIR /root  
  
#Copy pom.xml to /root  
# Prepare by downloading dependencies  
ADD pom.xml /root/pom.xml  
  
# Adding source, compile and package into a fat jar  
ADD src /root/src  
RUN mvn package  
  
#copy build war file to tomcat webapps  
RUN cp -r /root/target/hello-java-1.0.war /var/lib/tomcat8/webapps/  
RUN rm -rf /var/lib/tomcat8/webapps/ROOT  
  
# Launch Tomcat  
#CMD ["/var/lib/tomcat8/bin/catalina.sh", "run"]  
# Expose the default tomcat port  
EXPOSE 8080  
# Start the tomcat (and leave it hanging)  
#RUN service tomcat8 start  
# Define default command.  
CMD ["bash"]  
  
#adding comment  

