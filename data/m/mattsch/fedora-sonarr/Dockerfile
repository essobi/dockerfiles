FROM mattsch/fedora-rpmfusion:27  
MAINTAINER Matthew Schick <matthew.schick@gmail.com>  
  
# Run updates  
RUN dnf upgrade -yq && \  
dnf clean all  
  
# Install required packages  
RUN dnf install -yq mediainfo \  
mono-core \  
procps-ng \  
shadow-utils \  
tar \  
unrar && \  
dnf clean all  
  
# Set uid/gid (override with the '-e' flag), 1000/1000 used since it's the  
# default first uid/gid on a fresh Fedora install  
ENV LUID=1000 LGID=1000  
# Create the sonarr user/group  
RUN groupadd -g $LGID sonarr && \  
useradd -c 'Sonarr User' -s /bin/bash -m -d /opt/sonarr -g $LGID -u $LUID
sonarr  
  
# Grab the installer, do the thing  
RUN cd /tmp && \  
curl -qsSOL http://download.sonarr.tv/v2/master/mono/NzbDrone.master.tar.gz &&
\  
tar -xf NzbDrone.master.tar.gz -C /opt/ && \  
rm ./NzbDrone.master.tar.gz && \  
chown -R sonarr:sonarr /opt/NzbDrone  
  
# Need a config and storage volume, expose proper port  
VOLUME /config /storage  
EXPOSE 8989  
# Add script to copy default config if one isn't there and start sonarr  
COPY run-sonarr.sh update-sonarr.sh /bin/  
  
# Run our script  
CMD ["/bin/run-sonarr.sh"]  
  

