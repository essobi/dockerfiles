FROM ubuntu  
  
ARG DEBIAN_FRONTEND=noninteractive  
ENV XDG_CONFIG_HOME="/config" XDG_DATA_HOME="/config"  
ENV LANG='C.UTF-8' LANGUAGE='C.UTF-8' LC_ALL='C.UTF-8'  
ENV TERM="xterm"  
ENV DOCKER="YES"  
RUN \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y --no-install-recommends --no-install-suggests \  
apt-utils \  
apt-transport-https ca-certificates \  
build-essential \  
python \  
python-dev \  
python-pip \  
python-setuptools \  
nano \  
wget \  
curl \  
unzip \  
tzdata \  
htop && \  
  
# install s6-overlay  
curl -s -o - -L "https://github.com/just-
containers/s6-overlay/releases/download/v1.20.0.0/s6-overlay-amd64.tar.gz" |
tar xzf - -C /  
  
COPY requirements.txt /tmp/requirements.txt  
  
RUN pip install wheel && \  
pip install -r /tmp/requirements.txt  
  
RUN mkdir -p /app/syncwatch /volume1 /volume2 /opt /config  
  
RUN apt-get autoremove -y && \  
apt-get clean && rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
# create user  
RUN \  
useradd -u 1000 -U -d /config -s /bin/false abc && \  
usermod -G users abc  
  
# Copy Syncwatch to App Folder  
COPY ./syncwatch /app/syncwatch  
  
# Copy etc files  
COPY root/ /  
  
VOLUME ["/opt","/volume1","/volume2","/config"]  
WORKDIR /app/syncwatch  
  
ENTRYPOINT ["/init"]  

