FROM ubuntu:14.04  
#Packages  
RUN apt-get -y install curl apt-transport-https  
  
RUN echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a
/etc/apt/sources.list.d/sbt.list &&\  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823  
  
RUN apt-get update && apt-get -y install supervisor default-jdk git sbt  
  
RUN sbt update  
  
RUN apt-get -y install wget  
  
RUN mkdir /opt/hazel && wget -O /opt/hazel/hazelcast.jar
http://central.maven.org/maven2/com/hazelcast/hazelcast-all/3.5.3/hazelcast-
all-3.5.3.jar  
  
#clone tester  
RUN mkdir /opt/tester &&\  
cd /opt/tester/ &&\  
git clone https://github.com/dk14/cache-performance.git  
RUN cd /opt/tester/cache-performance && sbt test:package  
  
#configure  
COPY hazelcast.xml /etc/hazelcast.xml  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
EXPOSE 22 5701 5702 5703 5704 5705  
CMD ["/usr/bin/supervisord"]  

