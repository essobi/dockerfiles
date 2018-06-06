FROM centos:latest  
MAINTAINER Benedikt von St. Vieth  
  
# install dependencies and clean-up afterwards  
RUN yum -y update && yum install -y wget java-1.8.0-openjdk-headless && yum
clean all && rm -rf /var/lib/{rpm,yum}  
  
# install exist and cleanup  
RUN wget -q -O '/opt/exist.jar'
'http://downloads.sourceforge.net/project/exist/Stable/2.2/eXist-db-
setup-2.2.jar' && \  
echo 'INSTALL_PATH=/opt/exist' > '/opt/options.txt' && \  
java -jar '/opt/exist.jar' -options '/opt/options.txt' && \  
rm -f '/opt/exist.jar' '/opt/options'  
  
ADD entrypoint.sh /entrypoint.sh  
ENTRYPOINT /entrypoint.sh  
  
VOLUME /opt/exist/webapp/WEB-INF/data/  
  
EXPOSE 8080  

