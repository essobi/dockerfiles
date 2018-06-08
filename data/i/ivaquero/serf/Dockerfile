FROM alpine:3.4  
MAINTAINER Ignacio Vaquero Guisasola <i.vaqueroguisasola@gmail.com>  
  
LABEL org.label-schema.schema-version="1.0" \  
org.label-schema.version="0.8.0" \  
org.label-schema.description="Docker container with Hashicorp's Serf" \  
org.label-schema.name="serf" \  
org.label-schema.docker.cmd="docker run -d -p 7946:7946 -p 7373:7373
ivaquero/serf:0.8.0 agent -rpc-addr=0.0.0.0:7373"  
  
RUN apk update && \  
apk add ca-certificates=20160104-r4 && \  
apk add openssl=1.0.2j-r0 && \  
update-ca-certificates  
  
RUN wget -O /tmp/serf.zip
https://releases.hashicorp.com/serf/0.8.0/serf_0.8.0_linux_amd64.zip && \  
unzip /tmp/serf.zip -d /usr/bin/  
  
EXPOSE 7373 7946  
  
ENTRYPOINT ["serf"]  

