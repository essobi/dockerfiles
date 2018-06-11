FROM mattsch/fedora-rpmfusion:latest  
MAINTAINER William Brown  
  
# Install required packages  
RUN dnf install -yq git \  
python3 && \  
dnf clean all  
  
# Set uid/gid (override with the '-e' flag), 1000/1000 used since it's the  
# default first uid/gid on a fresh Fedora install  
ENV LUID=750 LGID=750  
# Create the watcher user/group  
RUN groupadd -g $LGID watcher && \  
useradd -c 'watcher User' -s /bin/bash -m -d /opt/watcher3 -g $LGID -u $LUID
watcher  
  
# Grab the installer, do the thing  
RUN git clone -q https://github.com/nosmokingbandit/watcher3.git
/opt/watcher3/app && \  
chown -R watcher:watcher /opt/watcher3  
  
# Need a config and storage volume, expose proper port  
VOLUME /config /log /downloads /movies /db /plugins  
EXPOSE 9090  
# Add script to copy default config if one isn't there and start nzbhydra  
COPY run-watcher.sh /bin/run-watcher.sh  
  
# Run our script  
CMD ["/bin/run-watcher.sh"]  
  

