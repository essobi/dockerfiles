FROM rethink/lhcb-baseline  
  
MAINTAINER robert.ende@fokus.fraunhofer.de  
  
#RUN apt-get install git maven default-jre default-jdk  
RUN cd /opt/reTHINK/dev-qos-support && git pull  
  
RUN cd /opt/reTHINK/dev-qos-support/lhcb && mvn clean install  
  
RUN cd /opt/reTHINK/dev-qos-support/lhcb/lhcb_broker/target && mv rethink-
lhcb-broker-*-jar-with-dependencies.jar rethink-lhcb-broker-jar-with-
dependencies.jar  
  
# change to lhcb dir for the broker to be able to use keystore from ssl folder  
RUN cd /opt/reTHINK/dev-qos-support/lhcb  
  
# ENTRYPOINT is the command that is always run.  
ENTRYPOINT ["java", "-jar", "/opt/reTHINK/dev-qos-
support/lhcb/lhcb_broker/target/rethink-lhcb-broker-jar-with-
dependencies.jar"]

