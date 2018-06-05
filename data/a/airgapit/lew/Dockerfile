FROM ubuntu:12.04  
MAINTAINER Kelly Plummer <kellyplummer@mac.com>  
  
# RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get upgrade -y  
  
EXPOSE 8080  
RUN apt-get -y install openjdk-7-jre openjdk-7-jdk  
RUN apt-get -y install curl  
RUN apt-get -y install bash  
RUN apt-get -y install unzip  
  
# Install Jetty  
ADD http://eclipse.org/downloads/download.php?file=/jetty/stable-8/dist/jetty-
distribution-8.1.16.v20140903.tar.gz&r=1 /opt/jetty.tar.gz  
RUN tar -xvf /opt/jetty.tar.gz -C /opt/  
RUN rm /opt/jetty.tar.gz  
RUN mv /opt/jetty-distribution-* /opt/jetty  
RUN rm -rf /opt/jetty/webapps.demo  
RUN useradd jetty -U -s /bin/false  
RUN chown -R jetty:jetty /opt/jetty  
  
# Install lew  
ADD https://bitbucket.org/codice/geoname-service/downloads/data.zip /data.zip  
RUN unzip /data.zip -d /  
  
ADD https://bitbucket.org/codice/geoname-
service/downloads/lew-0.2-20141015.211620-8.war /opt/jetty/webapps/root.war  
  
ENV MAVEN_OPTS "-Xmx2g"  
# Run Jetty  
ENTRYPOINT ["/opt/jetty/bin/jetty.sh", "supervise"]  
# CMD ["-Djetty.home=/opt/jetty"]  

