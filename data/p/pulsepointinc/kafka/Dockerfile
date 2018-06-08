FROM pulsepointinc/centos7-java8:latest  
  
COPY ./files/etc/yum.repos.d/confluent.repo /etc/yum.repos.d/confluent.repo  
  
RUN rpm --rebuilddb && \  
rpm --import http://packages.confluent.io/rpm/4.0/archive.key && \  
yum --disablerepo="*" \--enablerep="confluent" install -y confluent-
kafka-2.11.noarch && \  
yum clean all  

