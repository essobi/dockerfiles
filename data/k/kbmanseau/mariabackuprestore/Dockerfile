FROM debian:8  
#  
# Add user.  
#  
RUN \  
groupadd -g 666 mybackup && \  
useradd -u 666 -g 666 -d /backup -c "MySQL Backup User" mybackup  
  
#  
# Install required packages.  
#  
RUN \  
apt-get -y update && \  
apt-get -y install mydumper && \  
rm -rf /var/lib/apt/lists/*  
  
#  
# Install start script.  
#  
COPY backupscript.sh /init.sh  
COPY backupScriptVars.sh /initVars.sh  
RUN chmod 750 /init.sh  
  
#  
# Set container settings.  
#  
VOLUME ["/backup"]  
WORKDIR /backup  
  
#  
# Start process.  
#  
CMD ["/init.sh"]  

