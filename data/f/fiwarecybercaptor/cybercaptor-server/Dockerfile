############################################################  
# Dockerfile to build and run the FIWARE CyberCAPTOR Server  
# Based on Ubuntu  
############################################################  
# Use phusion/baseimage as base image. For more information,  
# see https://phusion.github.io/baseimage-docker/  
FROM phusion/baseimage:0.9.16  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Install dependencies to build XSB, build MulVAL, build the .war, install
python dependencies  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get -y upgrade && apt-get install -y \  
bison \  
flex \  
g++ \  
git \  
gcc \  
make \  
maven \  
openjdk-7-jdk \  
python-pip \  
sqlite3 \  
tomcat7 \  
wget \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Build XSB and move it to /opt/  
RUN mkdir -p /data/build/  
WORKDIR /data/build/  
RUN wget http://xsb.sourceforge.net/downloads/XSB360.tar.gz  
RUN tar xzf XSB360.tar.gz  
WORKDIR /data/build/XSB/build  
RUN ./configure  
RUN ./makexsb  
RUN cp -R /data/build/XSB/ /opt/XSB  
  
# Build MulVAL and move it to /opt/  
WORKDIR /data/build/  
RUN git clone https://github.com/fiware-cybercaptor/mulval.git  
WORKDIR /data/build/mulval  
ENV MULVALROOT=/data/build/mulval  
RUN make  
RUN cp -R /data/build/mulval /opt/mulval  
ENV MULVALROOT=/opt/mulval  
  
# Add the sources and build the Web Archive using Maven  
WORKDIR /data/build/  
RUN git clone -q https://github.com/fiware-cybercaptor/cybercaptor-server.git  
WORKDIR /data/build/cybercaptor-server  
RUN mvn package  
RUN mv ./target/cybercaptor-server*.war /var/lib/tomcat7/webapps/cybercaptor-
server.war  
  
# Add the python script and its dependencies  
WORKDIR /root/  
RUN git clone -q https://github.com/fiware-cybercaptor/cyber-data-
extraction.git  
WORKDIR /root/cyber-data-extraction  
RUN pip install -r requirements.txt  
  
# Add the necessary configuration files, the vulnerability database and test
inputs files  
RUN cp -R /data/build/cybercaptor-server/configuration-files
/root/.remediation  
ADD ./config.properties /root/.remediation/config.properties  
ADD ./inputs /root/.remediation/inputs  
RUN wget -O /root/.remediation/vulnerability-remediation-database.db
https://github.com/fiware-cybercaptor/cyber-data-
extraction/releases/download/4.4.1/vulnerability-remediation-database.db  
ENV VULNERABILITY_DATABASE_PATH /root/.remediation/vulnerability-remediation-
database.db  
  
# Clean up  
RUN rm -rf ~/.m2  
RUN rm -rf /data/  
  
# Prepare tomcat7  
ENV CATALINA_BASE=/var/lib/tomcat7  
ENV CATALINA_HOME=/usr/share/tomcat7  
RUN mkdir /var/lib/tomcat7/temp  
  
RUN mkdir /etc/service/tomcat7  
ADD tomcat7.sh /etc/service/tomcat7/run  
RUN chmod a+x /etc/service/tomcat7/run  
  
EXPOSE 8080  
WORKDIR /root/.remediation  

