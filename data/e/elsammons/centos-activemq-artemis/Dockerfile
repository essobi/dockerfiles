FROM centos:latest  
MAINTAINER Eric Sammons <elsammons@gmail.com>  
LABEL version="2.0.10" description="Creates an ActiveMQ/Artemis server on
CentOS Latest with a default test.queue available role=amq and allow-
anonymous"  
  
RUN useradd -U -m artemis  
#RUN mkdir /home/artemis/artemis-broker  
#RUN chmod 0770 /home/artemis /home/artemis/artemis-broker  
#RUN chgrp root /home/artemis /home/artemis/artemis-broker  
RUN yum -y update  
  
RUN yum install -y java-1.8.0-openjdk java-1.8.0-openjdk-devel wget epel-
release  
RUN yum install -y xmlstarlet libaio.x86_64 libaio-devel.x86_64 maven  
  
COPY pom.xml /  
#COPY run-artemis.sh /home/artemis/  
COPY run-artemis.sh /  
  
RUN mvn -U -Ddestdir=/opt clean generate-resources  
  
RUN /run-artemis.sh && mkdir /artemis-broker/lock && \  
chmod 1777 /artemis-broker/lock /artemis-broker/data  
  
EXPOSE 8161 61616 5445 5672 1883 61613  
USER artemis  
  
CMD cd /artemis-broker && \  
ls -l && \  
cd /artemis-broker/bin && \  
echo "Will attempt to start the broker now." && \  
./artemis run  

