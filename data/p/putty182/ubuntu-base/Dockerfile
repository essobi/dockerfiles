FROM ubuntu:16.04  
MAINTAINER putty182  
  
ARG UBUNTU_APT_MIRROR=http://archive.ubuntu.com/ubuntu  
ARG DEBIAN_FRONTEND=noninteractive  
ENV XDG_CONFIG_HOME="/config" \  
XDG_DATA_HOME="/config"  
ENV LANG='C.UTF-8' LANGUAGE='C.UTF-8' LC_ALL='C.UTF-8'  
# Setup repos and install packages  
RUN sed -i "s@http://archive.ubuntu.com/ubuntu@$UBUNTU_APT_MIRROR@g"
/etc/apt/sources.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
echo "deb http://download.mono-project.com/repo/ubuntu xenial main" | tee
/etc/apt/sources.list.d/mono-official.list && \  
apt-get update && \  
apt-get upgrade -y  
  
# Do more things  
RUN apt-get install -y \  
\--no-install-recommends \  
\--no-install-suggests \  
apt-transport-https \  
jq \  
curl \  
libcurl4-openssl-dev \  
ca-certificates-mono \  
mono-devel \  
sqlite3 \  
python \  
bzip2 \  
xz-utils \  
unrar \  
unzip \  
p7zip-full \  
wget \  
tzdata \  
xmlstarlet \  
uuid-runtime \  
udev \  
git \  
build-essential \  
python-dev \  
python-pip \  
ffmpeg \  
flac \  
mc  
  
# upgrade python  
RUN pip install --upgrade pip && \  
pip install --no-cache-dir -U setuptools  
  
# install latest mediainfo  
RUN wget "https://mediaarea.net/repo/deb/repo-mediaarea_1.0-5_all.deb" && \  
dpkg -i repo-mediaarea_1.0-5_all.deb && \  
apt-get update && \  
apt-get install -y mediainfo  
  
# install s6-overlay  
RUN curl -s -o /tmp/s6-overlay.tar.gz -L \  
"https://github.com/just-
containers/s6-overlay/releases/download/v1.19.1.1/s6-overlay-amd64.tar.gz" &&
\  
tar xzf /tmp/s6-overlay.tar.gz -C /  
  
# create user & make folders  
RUN useradd -u 1000 -U -d /config -s /bin/false plex && \  
usermod -G users plex && \  
mkdir -p \  
/app \  
/config \  
/transcode \  
/data  
  
# clean up  
RUN apt-get autoremove -y && \  
apt-get clean && \  
rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
COPY root/ /  
  
ENTRYPOINT ["/init"]  

