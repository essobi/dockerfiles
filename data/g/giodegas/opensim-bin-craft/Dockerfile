FROM giodegas/opensim-bin  
MAINTAINER Giovanni De Gasperis @giodegas  
  
# First script to execute  
COPY after_install.sh /sbin/after_install  
  
RUN apt-get update && apt-get -y install unzip ssh-client && \  
cd /opt && rm -fr opensim && \  
wget http://download.craft-world.org/0.8.2-craft-dev.zip && unzip 0.8.2-craft-
dev.zip && mv 0.8.2-craft-dev2 opensim && \  
chmod +x /sbin/after_install && \  
apt-get remove --purge -y $BUILD_PACKAGES && rm -rf /var/lib/apt/lists/*  
# Opensimulator ports  
EXPOSE 9000/tcp  
EXPOSE 9000/udp  

