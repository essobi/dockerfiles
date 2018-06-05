# based on https://github.com/mortiz/docker_ubuntu_novnc  
FROM chriamue/annotator:cpu  
MAINTAINER chriamue@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV SCREEN_DIMENSIONS 1024x768x16  
ENV DESKTOP_USERNAME annotator  
  
RUN apt-get update && apt-get install -y supervisor x11vnc wget git \  
net-tools tar gzip xvfb  
  
RUN useradd -ms /bin/bash ${DESKTOP_USERNAME} && \  
mkdir /home/${DESKTOP_USERNAME}/.vnc/ && \  
x11vnc -storepasswd ${DESKTOP_USERNAME} /home/${DESKTOP_USERNAME}/.vnc/passwd
&& \  
chown -R ${DESKTOP_USERNAME}:${DESKTOP_USERNAME}
/home/${DESKTOP_USERNAME}/.vnc && \  
chmod 0640 /home/${DESKTOP_USERNAME}/.vnc/passwd && \  
rm -rf /var/lib/apt/lists/*  
  
RUN git clone https://github.com/novnc/noVNC /noVNC  
  
COPY supervisor_annotator.conf /etc/supervisor/conf.d/annotator.conf  
  
EXPOSE 5900 6080  
CMD ["/usr/bin/supervisord", "-n"]  
  

