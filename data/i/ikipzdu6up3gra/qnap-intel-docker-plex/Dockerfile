FROM debian:stretch-slim  
  
# Install basic required packages.  
RUN set -x \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
apt-transport-https \  
apt-utils \  
ca-certificates \  
curl \  
dirmngr \  
dumb-init \  
nano \  
vim \  
wget \  
xmlstarlet \  
&& apt-get clean  
  
# Add Debian repos and Deb-Multimedia repo  
COPY root/etc/apt/sources.list /etc/apt/  
  
RUN set -x \  
# Install the Deb-Multimedia repo key  
&& cd /tmp \  
&& wget http://www.deb-multimedia.org/pool/main/d/deb-multimedia-keyring/deb-
multimedia-keyring_2016.8.1_all.deb \  
&& dpkg -i deb-multimedia-keyring_2016.8.1_all.deb \  
&& apt-get update \  
# Upgrade to get possible critical fixes.  
&& DEBIAN_FRONTEND=noninteractive apt-get upgrade -y --install-recommends \  
&& apt-get update \  
# Install all packages needed for hardware transcoding in Plex Media Server
for Intel i965 gfx cards  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --install-recommends \  
build-essential \  
debhelper \  
dnsutils \  
git \  
i965-va-driver \  
iputils-ping \  
libdrm-dev \  
libegl1-mesa-dev \  
libgl1-mesa-dev \  
libva-dev \  
libvdpau-va-gl1 \  
libvdpau1 \  
libwayland-dev \  
libx11-dev \  
libxext-dev \  
libxfixes-dev \  
lsb-release \  
lsof \  
mesa-utils \  
mesa-vdpau-drivers \  
net-tools \  
perl \  
pkg-config \  
software-properties-common \  
vainfo \  
vdpau-driver-all \  
vdpau-va-driver \  
vdpauinfo \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN set -x \  
# Create plex user  
&& useradd --system --uid 797 \--create-home --shell /usr/sbin/nologin plex \  
# Note: We created a dummy /bin/start to avoid install to fail due to upstart
not being installed.  
# We won't use upstart anyway.  
&& touch /bin/start \  
&& chmod +x /bin/start \  
&& touch /bin/stop \  
&& chmod +x /bin/stop \  
# Create writable config directory in case the volume isn't mounted  
&& mkdir /config \  
&& chown plex:plex /config  
  
# Download, compile, and install the latest Intel GFX libraries for hardware
transcoding  
RUN set -x \  
&& cd /tmp \  
&& /usr/bin/git clone https://github.com/01org/cmrt.git \  
&& /usr/bin/git clone https://github.com/01org/intel-hybrid-driver \  
&& /usr/bin/git clone https://github.com/01org/intel-vaapi-driver \  
&& /usr/bin/git clone https://github.com/01org/libva \  
&& /usr/bin/git clone https://github.com/01org/libva-utils \  
&& cd /tmp/cmrt \  
&& /bin/sh autogen.sh \  
&& /bin/sh configure \  
&& /usr/bin/make \  
&& /usr/bin/make install \  
&& cd /tmp/libva \  
&& /bin/sh autogen.sh \  
&& /bin/sh configure \  
&& /usr/bin/make \  
&& /usr/bin/make install \  
&& cd /tmp/libva-utils \  
&& /bin/sh autogen.sh \  
&& /bin/sh configure \  
&& /usr/bin/make \  
&& /usr/bin/make install \  
&& cd /tmp/intel-hybrid-driver \  
&& /bin/sh autogen.sh \  
&& /bin/sh configure \  
&& /usr/bin/make \  
&& /usr/bin/make install \  
&& cd /tmp/intel-vaapi-driver \  
&& /bin/sh autogen.sh \  
&& /bin/sh configure \  
&& /usr/bin/make \  
&& /usr/bin/make install \  
&& rm -Rf /tmp/*.deb \  
&& rm -Rf /tmp/cmrt \  
&& rm -Rf /tmp/intel-* \  
&& rm -Rf /tmp/libva* \  
# Plex Media Server has some hard-coded paths for video libs, so running
"vainfo" will not work without these symlink'ed  
&& mkdir -p /data/jenkins/pms-deps-universal-v2/BUILD_TAG/linux-
ubuntu-x86_64/output/pms-depends-linux-ubuntu-x86_64-release-87218f6/lib \  
&& ln -s /usr/local/lib/dri /data/jenkins/pms-deps-
universal-v2/BUILD_TAG/linux-ubuntu-x86_64/output/pms-depends-linux-
ubuntu-x86_64-release-87218f6/lib/dri  
# PLEX_MEDIA_SERVER_MAX_PLUGIN_PROCS: The number of plugins that can run at
the same time.  
# PLEX_MEDIA_SERVER_MAX_STACK_SIZE: Used for "ulimit -s
$PLEX_MEDIA_SERVER_MAX_STACK_SIZE".  
# PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR: defines the location of the
configuration directory,  
# default is "${HOME}/Library/Application Support".  
ENV PLEX_MEDIA_SERVER_MAX_PLUGIN_PROCS=6 \  
PLEX_MEDIA_SERVER_MAX_STACK_SIZE=3000 \  
PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR=/config \  
PLEX_MEDIA_SERVER_HOME=/usr/lib/plexmediaserver \  
LD_LIBRARY_PATH=/usr/lib/plexmediaserver \  
TMPDIR=/tmp \  
PLEXPASS_LOGIN='' \  
PLEXPASS_PASSWORD=''  
# Temporary workound  
# https://github.com/wernight/docker-plex-media-server/issues/38  
RUN ln -sf $(which true) /sbin/udevadm  
  
COPY root /  
  
VOLUME ["/config", "/media"]  
  
EXPOSE 32400  
  
WORKDIR /usr/lib/plexmediaserver  
ENTRYPOINT ["dumb-init", "/plex-autoupdate-entrypoint.sh"]  
CMD ["/install_run_plex.sh"]  

