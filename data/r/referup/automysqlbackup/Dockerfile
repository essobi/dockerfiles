FROM pataquets/automysqlbackup  
  
#RUN \  
# apt-get update && \  
# DEBIAN_FRONTEND=noninteractive \  
# apt-get install -y \  
# patch \  
# && \  
# apt-get clean && \  
#rm -rf /var/lib/apt/lists/*  
#  
#ADD 01_lock_tables.patch /usr/sbin/  
#ADD 02_ignore_tables.patch /usr/sbin/  
ADD ./automysqlbackup /usr/sbin/  
  
WORKDIR /usr/sbin  
  
#RUN \  
# patch automysqlbackup -i 01_lock_tables.patch && \  
# patch automysqlbackup -i 02_ignore_tables.patch  

