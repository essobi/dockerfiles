FROM ubuntu:16.04  
ADD
https://github.com/trapexit/mergerfs/releases/download/2.23.0/mergerfs_2.23.0.ubuntu-
trusty_amd64.deb /tmp/mergerfs.deb  
COPY ./entrypoint /entrypoint  
  
RUN chmod +x /entrypoint && dpkg -i /tmp/mergerfs.deb && rm /tmp/mergerfs.deb  
  
ENTRYPOINT ["/entrypoint"]  
ENV MERGERFS_OPTS="-o defaults,allow_other,use_ino" MERGERFS_SRC="/mnt/disk*"
MERGERFS_DEST="/mnt/data"  
HEALTHCHECK CMD ["ls /mnt/data"]  

