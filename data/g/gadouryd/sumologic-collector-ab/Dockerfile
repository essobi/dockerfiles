FROM sumologic/collector:latest-syslog  
MAINTAINER David Gadoury <dgadoury@sumologic.com>  
RUN sudo mkdir /root/docker  
RUN sudo mkdir /root/docker/configurations  
ADD https://s3.amazonaws.com/script-collection/docker/r1.0.0/Docker.bash
/root/docker/Docker.bash  
ADD https://s3.amazonaws.com/script-
collection/docker/r1.0.0/sumologic.properties
/root/docker/configurations/sumologic.properties  
ADD https://s3.amazonaws.com/script-collection/docker/r1.0.0/Sumo-Java-
APIIntegrationClient-1.0-SNAPSHOT.jar /root/docker/Sumo-Java-
APIIntegrationClient-1.0-SNAPSHOT.jar  
ADD sumo-sources.json /etc/sumo-sources.json  

