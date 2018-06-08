# gotchas/pharo-base64-vnc  
# for running interactive Pharo with VNC  
FROM gotchas/pharo-base64  
  
# Install LXDE, VNC server and Firefox  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -qy --no-install-recommends install \  
fluxbox \  
lxterminal \  
xfonts-base \  
tightvncserver  
# lxde-core \  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV USER root  
# Set default password  
COPY password.txt .  
RUN cat password.txt password.txt | vncpasswd -f > /opt/vncpasswd \  
&& rm password.txt  
  
# Expose VNC port  
EXPOSE 5901  
# Copy VNC script that handles restarts  
COPY vnc.sh /opt  
  
RUN chmod ugo+x /opt/vnc.sh  
CMD ["/opt/vnc.sh"]  

