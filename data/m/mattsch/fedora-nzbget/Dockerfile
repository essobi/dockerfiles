FROM mattsch/fedora-rpmfusion:latest  
MAINTAINER Matthew Schick <matthew.schick@gmail.com>  
  
# Run updates  
RUN dnf upgrade -yq && \  
dnf clean all  
  
# Install required packages  
RUN dnf install -yq procps-ng \  
python \  
tar \  
unrar && \  
dnf clean all  
  
# Set uid/gid (override with the '-e' flag), 1000/1000 used since it's the  
# default first uid/gid on a fresh Fedora install  
ENV LUID=1000 LGID=1000 NZBGET_VER=19.1  
# Create the nzbget user/group  
RUN groupadd -g $LGID nzbget && \  
useradd -c 'NZBGet User' -s /bin/bash -m -d /opt/nzbget -g $LGID -u $LUID
nzbget  
  
# Grab the installer, do the thing  
RUN cd /tmp && \  
curl -qOL
http://github.com/nzbget/nzbget/releases/download/v$NZBGET_VER/nzbget-$NZBGET_VER-
bin-linux.run && \  
sh ./nzbget-$NZBGET_VER-bin-linux.run --destdir /opt/nzbget && \  
rm ./nzbget-$NZBGET_VER-bin-linux.run && \  
chown -R nzbget:nzbget /opt/nzbget  
  
# Need a config and storage volume, expose proper port  
VOLUME /config /storage  
EXPOSE 6789  
# Add script to copy default config if one isn't there and start nzbget  
COPY run-nzbget.sh /bin/run-nzbget.sh  
  
# Run our script  
CMD ["/bin/run-nzbget.sh"]  
  

