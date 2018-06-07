FROM stakater/base-alpine:3.5  
LABEL authors="Hazim <hazim_malik@hotmail.com>"  
  
RUN apk add --no-cache ca-certificates apache2-utils  
  
COPY ./registry/registry /bin/registry  
COPY ./registry/config-example.yml /etc/docker/registry/config.yml  
  
VOLUME ["/var/lib/registry", "/etc/docker/registry/"]  
EXPOSE 5000  
# Simulate cmd behavior via environment variable  
# So that users are able to provice command line arguments to docker-registry  
ENV COMMAND "/etc/docker/registry/config.yml"  
# Make daemon service dir for docker-registry and place file  
# It will be started and maintained by the base image  
RUN mkdir -p /etc/service/docker-registry  
ADD start.sh /etc/service/docker-registry/run

