# Linux developer workstation  
# https://github.com/wendellmedina/dinuguan-workstation  
#  
# Pull base image.  
FROM dockerfile/ubuntu  
MAINTAINER Wendell Medina <wendellmedina@gmail.com>  
  
# Install LXDE and VNC server.  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y lxde-core lxterminal
tightvncserver && \  
rm -rf /var/lib/apt/lists/*  
# Define working directory.  
WORKDIR /data  
# Define default command.  
CMD ["bash"]  
# Expose ports.  
EXPOSE 5901  

