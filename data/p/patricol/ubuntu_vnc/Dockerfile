FROM patricol/ubuntu_supervisor:Cuda  
  
USER root  
  
# This should have VNC plus basic desktop environment.  
# VNC is the most reliable connection type, and the simplest to configure/fix.  
# When debugging adding compatibility for a new OS version, this is simpler
than noVNC/RDP, and also includes all the things needed to check that the
environment behaves as normal, before attempting to add compatibility for
additional connection methods.  
# This also allows for the more finicky noVNC/RDP images to build more
quickly; as desktop environment and some basic programs are are installed
here.  
RUN apt-get update; \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
tightvncserver \  
openbox obconf obmenu fonts-roboto \  
plank dbus-x11 \  
pwgen \  
xterm \  
mesa-utils && \  
# For testing glxgears etc.  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 5900  
ENV USER user  
RUN echo "PASSWORD=\\`pwgen -c -n -1 8\\`" >> /home/user/earlycommands.sh && \  
echo "echo -e \"Password: \$PASSWORD\" > /home/user/password.txt" >>
/home/user/earlycommands.sh && \  
echo "echo \"user:\$PASSWORD\" | chpasswd" >> /home/user/earlycommands.sh && \  
echo "su user -c \"mkdir -p ~/.vnc\"" >> /home/user/earlycommands.sh && \  
echo "su user -c \"echo '\$PASSWORD' | vncpasswd -f > ~/.vnc/passwd\"" >>
/home/user/earlycommands.sh && \  
echo "su user -c \"chown -R user:user ~/.vnc\"" >> /home/user/earlycommands.sh
&& \  
echo "su user -c \"chmod 600 ~/.vnc/passwd\"" >> /home/user/earlycommands.sh
&& \  
echo "su user -c \"touch ~/.Xresources\"" >> /home/user/earlycommands.sh && \  
echo "su user -c \"/usr/bin/tightvncserver :0\"" >>
/home/user/earlycommands.sh && \  
echo "su user -c \"/usr/bin/tightvncserver -kill :0\"" >>
/home/user/earlycommands.sh && \  
# Adds config files needed later by novnc etc.  
echo '#!/bin/bash\ncat /home/user/password.txt\nsupervisorctl start vnc:*' >
/home/user/vnc.sh && \  
chmod +x /home/user/vnc.sh  
  
#COPY --chown=root:root extras/vnc.conf /etc/supervisor/conf.d/#Not yet
supported by docker hub's automated builds, which use an outdated version of
docker.  
COPY extras/vnc.conf /etc/supervisor/conf.d/  
#COPY --chown=user:user extras/openbox-config/*
/home/user/.config/openbox/#Not yet supported by docker hub's automated
builds, which use an outdated version of docker.  
COPY extras/openbox-config/* /home/user/.config/openbox/  
#COPY --chown=user:user extras/*.dockitem
/home/user/.config/plank/dock1/launchers/#Not yet supported by docker hub's
automated builds, which use an outdated version of docker.  
COPY extras/*.dockitem /home/user/.config/plank/dock1/launchers/  
RUN chown -R user:user /home/user/.config/  
  
USER user

