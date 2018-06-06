FROM debian:stretch-slim  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive \  
apt-get install -y \  
coturn \  
curl \  
dumb-init \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY turnserver.sh /turnserver.sh  
  
USER "turnserver"  
VOLUME ["/conf"]  
EXPOSE 3478 3478/udp  
ENTRYPOINT ["dumb-init", "--", "/turnserver.sh"]  

