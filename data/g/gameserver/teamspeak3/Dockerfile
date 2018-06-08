############################################################  
# Dockerfile  
############################################################  
  
# Based on CentOS  
FROM centos:latest  
  
############################################################  
# Environment Configuration  
############################################################  
  
ENV TEAMSPEAK_VERSION=3.0.13.6  
ENV TEAMSPEAK_SERVERADMIN_PASSWORD superSecret  
  
############################################################  
# Installation  
############################################################  
  
# Copy Files  
COPY rootfs /  
  
# Setup  
RUN echo "Installing Packages ..." &&\  
# Install  
yum install -y curl bzip2 &&\  
# Permissions and Users  
chmod +x /usr/local/bin/entrypoint.sh &&\  
useradd -M -s /bin/false --uid 1000 teamspeak3  
  
# Download and extract Teamspeak 3  
RUN mkdir -p /server /data /data/logs &&\  
cd /server &&\  
curl -s
http://dl.4players.de/ts/releases/${TEAMSPEAK_VERSION}/teamspeak3-server_linux_amd64-${TEAMSPEAK_VERSION}.tar.bz2
-o teamspeak3-server.tar.bz2 &&\  
tar --strip-components=1 -xjf teamspeak3-server.tar.bz2 -C ./ &&\  
rm teamspeak3-server.tar.bz2 &&\  
chmod +x /server/ts3server_startscript.sh
/server/ts3server_minimal_runscript.sh &&\  
chown teamspeak3:teamspeak3 /server &&\  
chown teamspeak3:teamspeak3 /data  
  
############################################################  
# Execution  
############################################################  
  
# Volumes  
VOLUME ["/data"]  
  
# Working Directory  
WORKDIR /server  
  
# Entrypoint  
CMD ["/usr/local/bin/entrypoint.sh"]  

