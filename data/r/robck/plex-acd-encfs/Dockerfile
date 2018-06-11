FROM plexinc/pms-docker:latest  
  
LABEL org.label-schema.schema-version="1.0" \  
org.label-schema.name="plex-acd-encfs" \  
org.label-schema.description="Mount EncFS from Amazon Cloud Drive for Plex
using Docker." \  
org.label-schema.vcs-url="https://github.com/robck/acd-encfs.git" \  
org.label-schema.docker.cmd="docker run --cap-add SYS_ADMIN --device /dev/fuse
-e ENCFS6_PASSWORD='<EncFS Password>' -v
/local/path/to/.encfs6.xml:/etc/.encfs6.xml:ro -v
/local/path/to/acd_cli:/root/.cache/acd_cli -v robck/plex-acd-encfs" \  
org.label-schema.docker.param="ACD_ENCRYPTED_SUBDIR=Encrypted directory to
mount relative to ACD_MOUNT_SUBDIR, ACD_MOUNT_SUBDIR=ACD directory to mount,
ENCFS6_CONFIG=Location of EncFS config, ENCFS6_PASSWORD=Password for
decrypting EncFS, USER_UID=UID for mounted files, USER_GID=GID for mounted
files"  
  
# Install required packages  
ADD ["https://github.com/just-
containers/s6-overlay/releases/download/v1.19.1.1/s6-overlay-amd64.tar.gz", \  
"/tmp/"]  
  
ENTRYPOINT ["/init"]  
  
RUN \  
# Extract S6 overlay  
tar xzf /tmp/s6-overlay-amd64.tar.gz -C / && \  
  
apt-get -y update && \  
apt-get install -y \  
python3 \  
python3-pip \  
encfs \  
fuse \  
git \  
cron && \  
  
# Cleanup  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/* && \  
rm -rf var/tmp/*  
  
ADD ./s6 /etc/services.d  
  
RUN pip3 install --upgrade git+https://github.com/bgemmill/acd_cli.git  
  
RUN echo "user_allow_other" >> /etc/fuse.conf  
  
RUN mkdir /mnt/.acd/ mkdir /mnt/acd/  
  
ENV ACD_ENCRYPTED_SUBDIR="/" \  
ACD_MOUNT_SUBDIR="/" \  
ACD_CLI_CACHE_DIR="/root/.cache/acd_cli" \  
ENCFS6_CONFIG="/etc/.encfs6.xml" \  
ENCFS6_PASSWORD='' \  
MOUNT_UID="1000" \  
MOUNT_GID="1000"  

