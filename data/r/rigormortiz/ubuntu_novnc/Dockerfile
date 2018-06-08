FROM rigormortiz/ubuntu-supervisor:zesty  
  
MAINTAINER Mike Ortiz <mike@jellydice.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV NOVNC_VERSION 0.6.2  
ENV SCREEN_DIMENSIONS 1024x768x16  
ENV DESKTOP_USERNAME ubuntu  
  
RUN apt-get update -y && \  
apt-get install -y x11vnc wget git python python-numpy \  
net-tools tar gzip xvfb && \  
wget https://github.com/novnc/noVNC/archive/v${NOVNC_VERSION}.tar.gz && \  
tar -zxf v${NOVNC_VERSION}.tar.gz && mv noVNC-${NOVNC_VERSION} noVNC && \  
rm v${NOVNC_VERSION}.tar.gz && \  
apt-get autoclean && apt-get autoremove && \  
useradd -ms /bin/bash ${DESKTOP_USERNAME} && \  
mkdir /home/${DESKTOP_USERNAME}/.vnc/ && \  
x11vnc -storepasswd ${DESKTOP_USERNAME} /home/${DESKTOP_USERNAME}/.vnc/passwd
&& \  
chown -R ${DESKTOP_USERNAME}:${DESKTOP_USERNAME}
/home/${DESKTOP_USERNAME}/.vnc && \  
chmod 0640 /home/${DESKTOP_USERNAME}/.vnc/passwd && \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 5900 6080  
COPY supervisor_novnc.conf /etc/supervisor/conf.d/novnc.conf  

