FROM debian:stretch  
  
MAINTAINER Guillaume CONNAN "guillaume.connan44@gmail.com"  
  
LABEL version="0.1.4"  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV MC_VERSION 1.12.2  
  
RUN ( \  
echo "deb http://deb.debian.org/debian stretch main contrib non-free" \  
> /etc/apt/sources.list && \  
echo "deb http://deb.debian.org/debian stretch-updates main contrib non-free"
\  
>> /etc/apt/sources.list && \  
echo "deb http://security.debian.org stretch/updates main contrib non-free" \  
>> /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y -q upgrade && \  
apt-get -y -q dist-upgrade && \  
apt-get -y -q autoclean && \  
apt-get -y -q autoremove && \  
apt-get -y -q install sudo \  
build-essential \  
wget \  
git \  
python-pip \  
python-dev \  
python-imaging && \  
pip install Pillow numpy && \  
git clone --quiet \  
https://github.com/overviewer/Minecraft-Overviewer.git \  
/opt/overviewer && \  
( \  
cd /opt/overviewer && \  
python setup.py build \  
) && \  
mkdir -p /temp \  
/out && \  
groupadd -g 1000 overviewer && \  
useradd -u 1000 -s /bin/false -d /temp -g overviewer overviewer && \  
wget --quiet \  
\--directory-prefix /temp/.minecraft/versions/$MC_VERSION/ \  
https://s3.amazonaws.com/Minecraft.Download/versions/$MC_VERSION/$MC_VERSION.jar
&& \  
apt-get -y -q purge build-essential \  
wget \  
git \  
python-pip \  
python-dev && \  
apt-get -y -q autoremove && \  
apt-get clean && \  
rm -fr /tmp/* && \  
rm -fr /var/tmp/* && \  
rm -fr /var/lib/apt/lists/* \  
)  
  
ADD scripts/start.sh /start.sh  
  
# Expose volumes  
VOLUME ["/in", "/out"]  
  
# Init  
CMD ["/bin/bash", "/start.sh"]  

