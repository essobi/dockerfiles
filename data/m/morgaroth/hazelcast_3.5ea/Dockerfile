FROM ubuntu:14.04  
MAINTAINER Mateusz Jaje <mateuszjaje@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
RUN mkdir -p /opt/hazelcast  
WORKDIR /opt/hazelcast  
RUN apt-get -qqy update  
RUN apt-get -qqy install openjdk-7-jre-headless openjdk-7-jdk  
ADD
http://central.maven.org/maven2/com/hazelcast/hazelcast/3.5-EA/hazelcast-3.5-EA.jar
/opt/hazelcast/hazelcast-3.5-EA.jar  
ADD Start.java /opt/hazelcast/Start.java  
ADD hazelcast-conf.xml /opt/hazelcast/hazelcast-conf.xml  
ADD start.sh /opt/hazelcast/start.sh  
RUN chmod 755 /opt/hazelcast/start.sh  
RUN javac -cp "hazelcast-3.5-EA.jar" Start.java  
RUN apt-get --purge -qqy autoremove openjdk-7-jdk  
RUN apt-get clean  
EXPOSE 5701  
CMD /opt/hazelcast/start.sh  

