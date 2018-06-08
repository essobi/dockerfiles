FROM alpine:latest  
  
MAINTAINER Gwelican <superfly@gwelican.eu>  
  
RUN apk add --update mosquitto mosquitto-clients && \  
mkdir /work && chown 1000 /work  
  
VOLUME ["/work"]  
WORKDIR /work  
  
USER 1000  
EXPOSE 1883  
ENTRYPOINT ["mosquitto", "-c", "/work/mosquitto.conf"]  

