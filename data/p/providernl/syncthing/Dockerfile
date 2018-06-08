FROM ubuntu:16.04  
ENV SYNCTHING_VERSION v0.14.8  
ENV SYNCTHING_TARBALL syncthing-linux-amd64-$SYNCTHING_VERSION.tar.gz  
ENV SYNCTHING_HOME /home/syncthing/.config/syncthing  
ENV SYNCTHING_CONFIG $SYNCTHING_HOME/config.xml  
  
MAINTAINER Jeroen Boonstra <jeroen@provider.nl>  
  
# Install basic packages  
RUN apt-get update  
RUN apt-get install -y \  
\--no-install-recommends \  
ca-certificates \  
curl  
  
# gpg: key 00654A3E: public key "Syncthing Release Management
<release@syncthing.net>" imported  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
37C84554E7E0A261E4F76E1ED26E6ED000654A3E  
  
# Download syncthing  
RUN set -x \  
&& curl -fSL
"https://github.com/syncthing/syncthing/releases/download/$SYNCTHING_VERSION/"{"$SYNCTHING_TARBALL",sha1sum.txt.asc}
-O \  
&& gpg --verify sha1sum.txt.asc \  
&& grep -E " $SYNCTHING_TARBALL\$" sha1sum.txt.asc | sha1sum -c - \  
&& rm sha1sum.txt.asc \  
&& tar -xvf "$SYNCTHING_TARBALL" \--strip-components=1 "$(basename
"$SYNCTHING_TARBALL" .tar.gz)"/syncthing \  
&& mv syncthing /usr/local/bin/syncthing  
  
# Cleanup  
RUN set -x \  
&& apt-get purge -y --auto-remove curl \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm "$SYNCTHING_TARBALL"  
  
# Don't configure the default /Sync folder  
ENV STNODEFAULTFOLDER=true  
  
# Configure and run syncthing daemon  
COPY entrypoint.sh /  
ENTRYPOINT /entrypoint.sh  

