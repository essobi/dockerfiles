FROM quantumobject/docker-opensimulator  
MAINTAINER Giovanni De Gasperis @giodegas  
  
RUN apt-get update && \  
apt-get install -y tcpdump net-tools netcat vim && \  
apt-get remove --purge -y $BUILD_PACKAGES && rm -rf /var/lib/apt/lists/*  
# Opensimulator  
EXPOSE 9000/tcp  
EXPOSE 9000/udp  

