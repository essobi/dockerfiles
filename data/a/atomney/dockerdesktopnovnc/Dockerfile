FROM ubuntu:bionic  
LABEL maintainer="atomney+docker@gmail.com"  
  
# Tell APT that humans aren't going to answer package questions  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set a default Password for VNC  
ENV VNCPASS letmein  
  
# Copy start script into root of container  
COPY startup.sh /startup.sh  
  
# Install general packages  
RUN apt-get update -y && \  
apt-get install -y xfce4 xfce4-goodies tigervnc-standalone-server libglu1-mesa
git net-tools wget python python-numpy unzip firefox mtr-tiny remmina \  
iputils-ping geany htop tmux screen iperf netcat wireshark curl dnsutils snmp
zenmap telnet filezilla nano vim sshfs sudo traceroute autocutsel \  
sysstat openssh-server scrot pavucontrol openconnect && \  
apt-get remove -y xscreensaver && \  
apt-get autoclean -y && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  
# Install novnc  
RUN cd /root && git clone https://github.com/kanaka/noVNC.git && \  
cd /root && \  
chmod 0755 /startup.sh  
  
# Create non root user  
RUN adduser tux && \  
echo "tux ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/tux && \  
chmod 0440 /etc/sudoers.d/tux  
  
# Copy files into users home folder  
COPY xstartup /home/tux/.vnc/xstartup  
  
# Fix permissions on users home folder  
RUN chown -R tux:tux /home/tux && \  
chmod 0755 /home/tux/.vnc/xstartup  
  
# Set the script to run on container launch  
CMD /startup.sh  
  
# Expose the noVNC port  
EXPOSE 6080  

