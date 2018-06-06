FROM mesoform/concierge-alpine-base-image:latest  
  
# Add some labels  
LABEL maintainer="Daniel Perez <dan@mesoform.com>"  
LABEL description="Concierge maintained Consul Key Value Store Service
Discovery and Dynamic Configuration for Mesoform"  
LABEL com.mesoform.baseimage=False  
LABEL com.joyent.autopilotpattern=True  
LABEL com.mesoform.builddate="2018-03-05T19:01:20Z"  
LABEL com.mesoform.baseimage.ver="mesoform/concierge-alpine-base-image:latest"  
LABEL com.docker.img.ver="mesoform/concierge-consul:0.1.17"  
  
# Set some environment variables  
ENV DOCKER_IMG_VER="mesoform/concierge-consul:0.1.17"  
RUN unset CONSUL_AGENT  
ENV LOG_LEVEL="INFO"  
ENV LOG_FORMAT="text"  
ENV COMMAND="/usr/local/bin/consul agent -server -bootstrap-expect 1 -config-
dir /etc/consul -ui"  
# Add user-defined directories beyond default bin and etc  
COPY test /test/  
  
# If we have any install scripts, run them.  
RUN chmod -R +x /usr/local/bin/install.sh && \  
sync && \  
/usr/local/bin/install.sh  
  
# make directories  
RUN mkdir -p /data  
# define volumes if set  
VOLUME /data  
  
# Expose primary service port  
EXPOSE 8500  
# Expose additional container ports  
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 53 53/udp  
HEALTHCHECK \  
\--interval=10s \  
\--timeout=3s \  
\--retries=4 \  
CMD /usr/local/bin/consul-manage health  

