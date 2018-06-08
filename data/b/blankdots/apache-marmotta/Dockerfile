# apache marmotta  
FROM tomcat:7  
MAINTAINER blankdots <blankdots@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
# Install unzip  
RUN apt-get install -y unzip  
# Install curl  
RUN apt-get install -y curl  
RUN apt-get install -y openjdk-7-jdk  
  
WORKDIR /data/marmotta  
  
RUN curl -L http://www.apache.org/dyn/closer.cgi/marmotta/3.3.0/apache-
marmotta-3.3.0-webapp.zip -o apache-marmotta-3.3.0-webapp.zip  
  
RUN unzip -q apache-marmotta-3.3.0-webapp.zip  
  
WORKDIR /  
  
RUN rm -rf /usr/local/tomcat/webapps/ROOT/* \  
&& mv /data/marmotta/apache-marmotta-3.3.0/marmotta.war
/usr/local/tomcat/webapps/ROOT/ \  
&& cd /usr/local/tomcat/webapps/ROOT/ \  
&& jar -xvf marmotta.war  
  
ENV MATMOTTA_HOME /var/run/marmotta  
ENV JAVA_OPTS -Djava.net.preferIPv4Stack=true -Xmx2048 -XX:+UseConcMarkSweepGC
-XX:+CMSClassUnloadingEnabled -XX:+HeapDumpOnOutOfMemoryError  
  
COPY system-config.properties /var/run/marmotta/system-config.properties  
  
EXPOSE 8080  
#COPY ./startup.sh /startup.s  
#RUN chmod +x /startup.sh  
#CMD ["/startup.sh"]

