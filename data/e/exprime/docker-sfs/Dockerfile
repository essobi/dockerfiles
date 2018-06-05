FROM ubuntu:16.04  
RUN apt-get update && \  
apt-get --quiet --yes install rsync \  
fuse \  
build-essential \  
git \  
php \  
libfuse-dev \  
pkg-config && \  
mkdir -p /home/sfs /mnt/data /mnt/batches/tmp /mnt/fuse && \  
cd /home/sfs && \  
git clone https://github.com/immobiliare/sfs && \  
cd /home/sfs/sfs/fuse && \  
make -j && \  
cp /home/sfs/sfs/fuse/sfs /usr/local/bin/ && \  
echo "sfs#/mnt/data /mnt/fuse fuse noatime,allow_other,sfs_perms 0 0" >>
/etc/fstab && \  
apt-get clean  
COPY config.php /home/sfs/sfs/php-sync/config.php  
COPY sfs.conf /mnt/data/.sfs.conf  
EXPOSE 8173  
CMD sfs --perms -o kernel_cache,use_ino /mnt/data /mnt/fuse & php
/home/sfs/sfs/php-sync/sync.php

