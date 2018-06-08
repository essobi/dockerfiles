##############################  
# Alfred Centos 7 Base  
# Tag: kanalfred/fileserver  
#  
# Refer:  
# https://www.youtube.com/watch?v=DIlqpSoftOo  
# https://github.com/marcelmaatkamp/docker-alpine-
radius/blob/master/Dockerfile  
# https://computingforgeeks.com/installing-freeradius-and-daloradius-centos-7/  
#  
# Run:  
# docker run --name test-radius -p 1812:1812/udp -p 1813:1813/udp -p
18120:18120 -d kanalfred/radius  
# docker run --name radius -p 1812:1812/udp -p 1813:1813/udp -p 18120:18120 -v
/data/radius/raddb/mods-available/sql:/etc/raddb/mods-available/sql -d
kanalfred/radius  
#  
# Build:  
# docker build -t kanalfred/radius .  
#  
# Steps:  
# 1) update sql host connection string /data/radius/raddb/mods-available/sql
and mount to container  
# 2) [Optional] update vpn host ip in /data/radius/raddb/client.conf and mount
to container  
#  
# Test:  
# radtest alfred landmark5! localhost 0 landmark5!  
# docker exec -it test-radius radtest alfred landmark5! localhost 0 landmark5!  
#  
# Dependancy:  
# Centos 7  
#  
# Crontab config:  
# mount:  
# /root/.dropbox (to prisist the linked account config)  
# /root/Dropbox (dir want to sync)  
#  
##############################  
  
FROM kanalfred/centos7:latest  
MAINTAINER Alfred Kan <kanalfred@gmail.com>  
  
# Add Files  
#/etc/cron.d  
#ADD container-files/config /config  
  
RUN \  
yum -y install \  
nfs-utils \  
mysql \  
vim \  
freeradius freeradius-utils freeradius-mysql  
# yum clean all && \  
  
ADD container-files/etc /etc  
  
# user & permission  
RUN \  
groupadd -g 1000 -r hostadmin \  
&& useradd -u 1000 -r -g hostadmin hostadmin \  
#&& chown -R hostadmin:hostadmin /sync \  
&& usermod -a -G root hostadmin  
  
#/usr/sbin/radiusd -d /etc/raddb  
  
RUN \  
ln -s /etc/raddb/mods-available/sql /etc/raddb/mods-enabled/ \  
&& chgrp -h radiusd /etc/raddb/mods-enabled/sql  
  
# Clean YUM caches to minimise Docker image size  
RUN yum clean all && rm -rf /tmp/yum*  
  
# EXPOSE  
EXPOSE \  
1812/udp \  
1813/udp \  
18120  
  
#CMD ["radiusd","-xx","-f"]  

