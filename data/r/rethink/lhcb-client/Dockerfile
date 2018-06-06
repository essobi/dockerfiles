FROM rethink/lhcb-baseline  
  
MAINTAINER robert.ende@fokus.fraunhofer.de  
  
#RUN apt-get install git maven default-jre default-jdk  
RUN cd /opt/reTHINK/dev-qos-support && git pull  
  
RUN cd /opt/reTHINK/dev-qos-support/lhcb && mvn clean install  
  
RUN cd /opt/reTHINK/dev-qos-support/lhcb/lhcb_client/target && mv rethink-
lhcb-client-*-jar-with-dependencies.jar rethink-lhcb-client-jar-with-
dependencies.jar  
  
# ENTRYPOINT is the command that is always run.  
ENTRYPOINT ["java", "-jar", "/opt/reTHINK/dev-qos-
support/lhcb/lhcb_client/target/rethink-lhcb-client-jar-with-
dependencies.jar"]

