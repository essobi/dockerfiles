FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
CMD /startup.sh  
EXPOSE 6080  
# Base packages for noVNC  
RUN apt-get update -y && \  
apt-get install -y git x11vnc wget python python-numpy unzip xvfb openbox menu
net-tools && \  
cd /root && git clone https://github.com/kanaka/noVNC.git && \  
cd noVNC/utils && git clone https://github.com/kanaka/websockify websockify  
  
RUN apt-get install -y baobab  
ADD startup.sh /startup.sh  
  
# Make things executable and clean up  
RUN cd /root && \  
chmod 0755 /startup.sh && \  
apt-get autoclean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  

