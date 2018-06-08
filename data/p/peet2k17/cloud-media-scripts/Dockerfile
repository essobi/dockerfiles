####################  
# BASE IMAGE  
####################  
FROM ubuntu:16.04  
  
MAINTAINER prc2k10@googlemail.com <prc2k10@googlemail.com>  
  
  
####################  
# INSTALLATIONS  
####################  
RUN apt-get update && apt-get install -y \  
curl \  
fuse \  
unionfs-fuse \  
bc \  
unzip \  
wget  
  
RUN apt-get update && apt-get install -y ca-certificates && update-ca-
certificates && apt-get install -y openssl  
RUN sed -i 's/#user_allow_other/user_allow_other/' /etc/fuse.conf  
  
# S6 overlay  
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2  
ENV S6_KEEP_ENV=1  
  
RUN \  
OVERLAY_VERSION=$(curl -sX GET "https://api.github.com/repos/just-
containers/s6-overlay/releases/latest" \  
| awk '/tag_name/{print $4;exit}' FS='[""]') && \  
curl -o \  
/tmp/s6-overlay.tar.gz -L \  
"https://github.com/just-
containers/s6-overlay/releases/download/${OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz" && \  
tar xfz \  
/tmp/s6-overlay.tar.gz -C /  
  
  
####################  
# ENVIRONMENT VARIABLES  
####################  
# Encryption  
ENV ENCRYPT_MEDIA "1"  
  
# Read Only  
ENV READ_ONLY "1"  
  
# Use "plexdrive" or rclone (cache) Set to "cache" if using rclone cache  
ENV CACHE_PROGRAM "plexdrive"  
  
# Rclone  
ENV BUFFER_SIZE "512M"  
ENV CHECKERS "16"  
ENV RCLONE_CLOUD_ENDPOINT "gd-crypt:"  
ENV RCLONE_LOCAL_ENDPOINT "local-crypt:"  
ENV RCLONE_VERBOSE "0"  
ENV RCLONE_LOG_LEVEL "NOTICE"  
ENV RCLONE_REMOTE_CONTROL "0"  
  
# Rclone Cache Settings  
ENV RCLONE_CACHE_ENDPOINT "gd-cache:"  
ENV RCLONE_CACHE_WRITE_ENDPOINT "gd-cache-write:"  
ENV RCLONE_CACHE_DIRECTWRITE "0"  
ENV CACHE_CHUNK_SIZE "5M"  
ENV CACHE_TOTAL_CHUNK_SIZE "10G"  
ENV CACHE_INFO_AGE "6h"  
ENV CACHE_WORKERS "4"  
ENV RCLONE_CACHE_PURGE "0"  
ENV RCLONE_V_CACHE_MODE "off"  
ENV RCLONE_V_CACHE_MAX_AGE_DURATION "1h0m0s"  
  
# Rclone Mirror Settings  
ENV MIRROR_MEDIA "0"  
ENV RCLONE_MIRROR_ENDPOINT "gdm-crypt:"  
ENV ENCRYPT_MIRROR_MEDIA "1"  
ENV MIRROR_BWLIMIT "100M"  
ENV MIRROR_TRANSFERS "4"  
ENV MIRROR_TPS_LIMIT "1"  
ENV MIRROR_TPS_LIMIT_BURST "1"  
  
# Plexdrive  
ENV CHUNK_SIZE "10M"  
ENV CHUNK_CHECK_THREADS "2"  
ENV CHUNK_LOAD_THREADS "2"  
ENV CHUNK_LOAD_AHEAD "3"  
ENV MAX_CHUNKS "10"  
  
# Time format  
ENV DATE_FORMAT "+%F@%T"  
  
# Local files removal  
ENV REMOVE_LOCAL_FILES_BASED_ON "space"  
ENV REMOVE_LOCAL_FILES_WHEN_SPACE_EXCEEDS_GB "100"  
ENV FREEUP_ATLEAST_GB "80"  
ENV REMOVE_LOCAL_FILES_AFTER_DAYS "30"  
  
####################  
# SCRIPTS  
####################  
COPY setup/* /usr/bin/  
  
COPY install.sh /  
  
COPY scripts/* /usr/bin/  
  
RUN chmod a+x /install.sh  
RUN sh /install.sh  
RUN chmod a+x /usr/bin/*  
  
COPY root /  
  
# Create abc user  
RUN groupmod -g 1000 users && \  
useradd -u 911 -U -d / -s /bin/false abc && \  
usermod -G users abc  
  
####################  
# VOLUMES  
####################  
# Define mountable directories.  
VOLUME /config /cloud-encrypt /cloud-decrypt /local-decrypt /local-media
/chunks /log  
  
RUN chmod -R 777 /log  
  
####################  
# WORKING DIRECTORY  
####################  
WORKDIR /  
  
  
####################  
# ENTRYPOINT  
####################  
ENTRYPOINT ["/init"]  

