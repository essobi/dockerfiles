FROM mattsch/fedora-rpmfusion:27  
MAINTAINER Matthew Schick <matthew.schick@gmail.com>  
  
# Run updates  
RUN dnf upgrade -yq && \  
dnf clean all  
  
# Install required packages  
RUN dnf install -yq mediainfo \  
mono-core \  
mono-locale-extras \  
procps-ng \  
shadow-utils \  
tar \  
unrar && \  
dnf clean all  
  
# Set uid/gid (override with the '-e' flag), 1000/1000 used since it's the  
# default first uid/gid on a fresh Fedora install  
ENV LUID=1000 LGID=1000  
# Create the radarr user/group  
RUN groupadd -g $LGID radarr && \  
useradd -c 'Radarr User' -s /bin/bash -m -d /opt/Radarr \  
-g $LGID -u $LUID radarr  
  
# Grab the installer, do the thing  
RUN cd /tmp && \  
export TAG=$(curl -qsX GET \  
https://api.github.com/repos/Radarr/Radarr/releases \  
| awk '/tag_name/{print $4;exit}' FS='[""]') && \  
curl -qsSL -o /tmp/radarr.tar.gz \  
https://github.com/galli-
leo/Radarr/releases/download/${TAG}/Radarr.develop.${TAG#v}.linux.tar.gz && \  
cd /opt/ && \  
tar xf /tmp/radarr.tar.gz && \  
rm /tmp/radarr.tar.gz && \  
chown -R radarr:radarr /opt/Radarr  
  
# Need a config and storage volume, expose proper port  
VOLUME /config /storage  
EXPOSE 7878  
# Add script to copy default config if one isn't there and start radarr  
COPY run-radarr.sh update-radarr.sh /bin/  
  
# Run our script  
CMD ["/bin/run-radarr.sh"]  

