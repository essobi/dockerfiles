## PMS-DOCKER  
# plexinc/pms-docker https://github.com/plexinc/pms-docker  
## ACD_CLI  
# https://github.com/pwntr/acd_cli-alpine-docker  
  
FROM plexinc/pms-docker  
  
# ACD_CLI | set the cache, settings, and libfuse path accordingly  
ENV ACD_CLI_CACHE_PATH /acd_cli/cache  
ENV ACD_CLI_SETTINGS_PATH /acd_cli/config  
ENV LIBFUSE_PATH /lib/x86_64-linux-gnu/libfuse.so.2  
  
RUN \  
mkdir -p \  
/acd_cli/config \  
/acd_cli/cache \  
/media/acd \  
/media/local \  
/media/.acd \  
/media/.local \  
/media/.index && \  
chmod -R 777 /acd_cli && \  
chmod -R 777 /media  
  
RUN \  
# Update and get dependencies  
apt-get update && \  
apt-get install -y \  
cifs-utils \  
nfs-common \  
fuse \  
unionfs-fuse \  
libfuse-dev \  
python3 python3-appdirs python3-dateutil python3-requests python3-sqlalchemy
python3-pip \  
git  
  
# ACD_CLI | install acd_cli  
RUN \  
pip3 install --upgrade pip && \  
pip3 install --upgrade git+https://github.com/yadayada/acd_cli.git  
  
RUN \  
#Cleanup  
apt-get -y remove git && \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/*  
  
# Extra ENV  
ENV ACD_CLI_MOUNT_CACHE_PATH /acd_cli/mount-cache  
  
# COPY root/ /  
COPY root/ /  
  
#COPY root/ /  
#CMD ["/bin/bash", "/helloworld.sh"]  

