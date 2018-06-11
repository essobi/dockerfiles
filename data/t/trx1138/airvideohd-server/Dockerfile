FROM debian:stretch-slim  
# Build arguments  
ARG VCS_REF  
ARG VERSION  
ARG AVSERVERHD_VERSION="2.2.3"  
ARG DEBIAN_FRONTEND="noninteractive"  
# Set label metadata  
LABEL org.label-schema.name="airvideohd-server-daemon" \  
org.label-schema.description="Alpine Linux Docker Container running AirVideo
HD Server streamer / transcoder" \  
org.label-schema.usage="https://github.com/madcatsu/docker-airvideohd-server-
daemon/blob/master/README.md" \  
org.label-schema.url="https://github.com/madcatsu/docker-airvideohd-server-
daemon" \  
org.label-schema.version=$VERSION \  
org.label-schema.vcs-url="https://github.com/madcatsu/docker-airvideohd-
server-daemon" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="1.0"  
# global environment settings  
ENV LANG C.UTF-8  
# Install packages  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
avahi-daemon \  
bash \  
bsdtar \  
curl \  
dbus \  
python3-minimal \  
python3-pkg-resources \  
python3-pip \  
python3-setuptools \  
wget \  
vlc-nox && \  
# Install Chaperone  
pip3 install --no-cache --upgrade \  
pip \  
setuptools \  
wheel \  
chaperone && \  
# Prep directories  
mkdir -p \  
/config \  
/defaults \  
/logs \  
/media \  
/opt/airvideohd \  
/transcode \  
/tmp/packages \  
/var/run/avahi-daemon \  
/var/run/dbus && \  
wget -qO- \  
"https://s3.amazonaws.com/AirVideoHD/Download/AirVideoServerHD-${AVSERVERHD_VERSION}.tar.bz2"
\  
| bsdtar -xf- -C /tmp/packages && \  
mv \  
/tmp/packages/AirVideoServerHD \  
/tmp/packages/Resources \  
/opt/airvideohd && \  
mv \  
/tmp/packages/Server.properties \  
/defaults && \  
# Cleanup  
apt autoremove -y \  
bsdtar \  
python3-pip \  
python3-setuptools \  
wget && \  
rm -rf \  
/tmp/packages \  
/var/lib/apt/lists/*  
# copy local files  
COPY /root /  
# ports and volumes  
EXPOSE 45633 45633/udp 5353/udp  
VOLUME ["/config","/media","/logs","/transcode"]  
ENTRYPOINT ["/usr/local/bin/chaperone","--default-home","/config"]  

