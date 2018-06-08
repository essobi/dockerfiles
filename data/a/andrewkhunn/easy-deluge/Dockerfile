# Base Image  
FROM ubuntu  
  
ARG DEBIAN_FRONTEND=noninteractive  
ENV LANG='C.UTF-8' LANGUAGE='C.UTF-8' LC_ALL='C.UTF-8'  
# ADD necessary stuff  
ADD https://github.com/Nottt/easy-
deluge/releases/download/1.1.5/libtorrent-1.1.5-1_amd64.deb
/root/libtorrent.deb  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.21.1.1/s6-overlay-amd64.tar.gz
/tmp/  
ADD https://downloads.rclone.org/rclone-current-linux-amd64.zip /tmp/  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /  
COPY files/ /root  
  
RUN apt-get update && apt install -y \  
libboost-system-dev \  
libboost-python-dev \  
libboost-chrono-dev \  
libboost-random-dev \  
libssl-dev \  
unrar \  
software-properties-common \  
apt-utils \  
wget \  
unzip \  
p7zip-full \  
ffmpeg \  
python-pip && \  
  
# Add necessary stuff for mp4 automation  
  
pip install setuptools && \  
pip install requests && \  
pip install requests[security] && \  
pip install requests-cache && \  
pip install babelfish && \  
pip install "guessit<2" && \  
pip install "subliminal<2" && \  
pip uninstall -y stevedore && \  
pip install stevedore==1.19.1 && \  
pip install python-dateutil && \  
pip install deluge-client && \  
pip install qtfaststart && \  
pip install gevent && \  
  
# Compile  
  
dpkg -i /root/libtorrent.deb && \  
apt-get install -f && \  
ldconfig && \  
  
# ADD Deluge PPA to keep always updated and install deluge  
add-apt-repository ppa:deluge-team/ppa -y && \  
apt-get update && \  
apt-get install deluged deluge-web deluge-console -y && \  
  
# Create necessary folders  
  
mkdir -p /config /downloads && \  
  
# Create user and set permissions  
  
adduser --disabled-login --no-create-home --gecos "" deluge && \  
usermod -G users deluge && \  
  
# Cleanup  
  
apt remove software-properties-common apt-utils -y && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/* /root/libtorrent.deb  
  
# Copy S6 init scripts  
COPY s6/ /etc  
  
EXPOSE 8112 58846 50000 50000/udp  
VOLUME /config /downloads  
  
ENTRYPOINT ["/init"]  

