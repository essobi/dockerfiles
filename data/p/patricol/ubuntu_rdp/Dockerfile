FROM patricol/compile:xrdp as xrdp_all  
FROM scratch as xrdp  
COPY \--from=xrdp_all /1604/ /  
FROM patricol/ubuntu_novnc:Cuda  
  
USER root  
  
RUN apt-get update; \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
pulseaudio xauth && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY \--from=xrdp / /tmp/install-xrdp/  
RUN /tmp/install-xrdp/install-xrdp.sh  
  
#COPY --chown=root:root extras/asound.conf /etc/asound.conf#Not yet supported
by docker hub's automated builds, which use an outdated version of docker.  
COPY extras/asound.conf /etc/asound.conf  
#COPY --chown=root:root extras/rdp.conf /etc/supervisor/conf.d/#Not yet
supported by docker hub's automated builds, which use an outdated version of
docker.  
COPY extras/rdp.conf /etc/supervisor/conf.d/  
  
EXPOSE 3389  
RUN cp /etc/X11/xrdp/xorg.conf /etc/X11 && \  
sed -i "s/xrdp\/xorg/xorg/g" /etc/xrdp/sesman.ini && \  
echo "openbox-session" > /home/user/.xsession && \  
echo "echo \"export QT_XKB_CONFIG_ROOT=/usr/share/X11/locale\" >>
/etc/profile" >> /home/user/earlycommands.sh && \  
echo '#!/bin/bash\ncat /home/user/password.txt\nsupervisorctl start rdp:*' >
/home/user/rdp.sh && \  
chmod +x /home/user/rdp.sh && \  
echo '#!/bin/bash\necho "only run this from an rdp gui terminal."\nwget
http://www.kozco.com/tech/piano2.wav\npaplay piano2.wav' >
/home/user/test_sound.sh && \  
chmod +x /home/user/test_sound.sh  
  
USER user

