FROM ubuntu:16.04  
ENV SYNCTHING_INOTIFY_VERSION v0.8.3  
ENV SYNCTHING_INOTIFY_TARBALL syncthing-inotify-linux-
amd64-$SYNCTHING_INOTIFY_VERSION.tar.gz  
ENV SYNCTHING_HOME /home/syncthing/.config/syncthing  
  
MAINTAINER Jeroen Boonstra <jeroen@provider.nl>  
  
# Install basic packages  
RUN apt-get update  
RUN apt-get install -y \  
\--no-install-recommends \  
ca-certificates \  
curl  
  
# Download syncthing-inotify  
RUN set -x \  
&& curl -fSL "https://github.com/syncthing/syncthing-
inotify/releases/download/$SYNCTHING_INOTIFY_VERSION/$SYNCTHING_INOTIFY_TARBALL"
-O \  
&& apt-get purge -y --auto-remove curl \  
&& tar -xvf "$SYNCTHING_INOTIFY_TARBALL" syncthing-inotify \  
&& mv syncthing-inotify /usr/local/bin/syncthing-inotify  
  
# Cleanup  
RUN set -x \  
&& apt-get purge -y --auto-remove curl \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm "$SYNCTHING_INOTIFY_TARBALL"  
  
# Run syncthing-inotify  
ENTRYPOINT syncthing-inotify -home=$SYNCTHING_HOME  

