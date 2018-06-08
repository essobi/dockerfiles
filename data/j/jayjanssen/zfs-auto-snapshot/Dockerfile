FROM ubuntu:xenial  
  
RUN apt-get update && apt-get dist-upgrade -y  
RUN apt-get install -y zfsutils-linux cron  
RUN apt-get install -y wget unzip cron  
RUN rm -rf /var/lib/apt/lists/*  
  
# Remove zfsutils-linux cron as it likely exists in the host  
RUN rm -f /etc/cron.d/zfsutils-linux  
  
RUN wget https://github.com/zfsonlinux/zfs-auto-snapshot/archive/master.zip  
RUN unzip master.zip -d /tmp  
WORKDIR /tmp/zfs-auto-snapshot-master  
RUN make install PREFIX=/usr  
  
WORKDIR /  
  
CMD /usr/sbin/cron -f -l  
  

