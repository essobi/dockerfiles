#  
# Jenkins CI Tool: Latest Version available from Docker Hub.  
#  
# https://github.com/lumagate/jenkins  
#  
# TRIGGER  
# Pull latest jenkins base image.  
FROM jenkins:latest  
  
# Maintainer contact information.  
MAINTAINER Ryan Irujo <ryan.irujo@gmail.com>  
  
# Changing over to root user.  
USER root  
  
# Installing latest versions of npm, node, nodejs, net-tools, sudo, and vim.  
RUN apt-get update && apt-get install -y \  
npm \  
node \  
nodejs \  
net-tools \  
sudo \  
vim && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Addinng sudo entry for the jenkins user in the file /etc/sudoers.d/jenkins.  
RUN touch /etc/sudoers.d/jenkins && \  
echo "jenkins ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/jenkins && \  
chmod 440 /etc/sudoers.d/jenkins  
  
# Setting xterm configuration.  
RUN touch /etc/profile.d/set_term.sh && \  
echo "export TERM=xterm-color" > /etc/profile.d/set_term.sh && \  
. /etc/profile  
  
# Changing back over to the User jenkins.  
USER jenkins  
  
# Exposing Port 80 for NodeJS Application. (Prod)  
EXPOSE 80  
# Exposing Port 5000 for NodeJS Application. (Test)  
EXPOSE 5000  
# Exposing Port 8080 for Jenkins Web Interface.  
EXPOSE 8080  
# Exposing Port 50000 for use by any attached Slave Agents.  
EXPOSE 50000  
# Default command to start Jenkins.  
CMD ["/bin/tini", "--", "/usr/local/bin/jenkins.sh"]  

