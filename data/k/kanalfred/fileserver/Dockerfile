##############################  
# Alfred Centos 7 Base  
# Tag: kanalfred/fileserver  
#  
# Refer:  
# https://www.howtoforge.com/samba-server-installation-and-configuration-on-
centos-7  
# cron issue  
# http://stackoverflow.com/questions/31644391/docker-centos-7-cron-not-
working-in-local-machine  
#  
# Run:  
# docker run -e 'ROOT_PASSWORD=test123' -h fileserver --name fileserver -p
2201:22 -d kanalfred/fileserver  
# docker run -h fileserver --name fileserver -p 2201:22 -p 445:445 -p 139:139
-p 135:135 -p 137:137/udp -p 138:138/udp -d kanalfred/fileserver  
# docker run -h fileserver --name fileserver --volumes-from data-fileserver
--volumes-from data-fileserver-bak --volumes-from data-other -p 2200:22 -p
445:445 -p 139:139 -p 135:135 -p 137:137/udp -p 138:138/udp --restart always
-d kanalfred/fileserver  
#  
# Build:  
# docker build -t kanalfred/fileserver .  
#  
# Create volume container:  
# [local]  
# docker create -v
/home/alfred/workspace/docker/data/fileserver/mnt/storage:/mnt/storage --name
data-fileserver centos:7  
# docker create -v
/home/alfred/workspace/docker/data/fileserver/mnt/storage_bak:/mnt/storage_bak
--name data-fileserver-bak centos:7  
# [coreos]  
# docker create -v /mnt/storage:/mnt/storage --name data-fileserver centos:7  
# docker create -v /mnt/storage_bak:/mnt/storage_bak --name data-fileserver-
bak centos:7  
# docker create -v /mnt/other:/mnt/other --name data-other centos:7  
#  
# Dependancy:  
# Centos 7  
#  
# Crontab config:  
# /etc/cron.d/  
#  
# Add samba users:  
# 1) add user  
# smbpasswd -a share  
# 2) export new smb password file  
# ######pdbedit -e smbpasswd:/root/samba-users.backup # (doesn't work)  
# sudo pdbedit -L -w > /root/samba-users.backup  
# 3) replace with new export samba-users.backup to config/samba-users.backup  
#  
# To import samba password file:  
# pdbedit -i smbpasswd:/root/samba-users.backup  
#  
# Check samba users:  
# sudo pdbedit -L -v  
#  
# supervisord Nondaemonizing of Subprocesses  
# http://supervisord.org/subprocess.html#nondaemonizing-of-subprocesses  
#  
# fileserver (same hd sync)  
# filesync (backup server to seperate hd)  
# openvpn  
# dns  
# workspace  
# web  
# mail  
# mysql  
# couchbase  
# git  
##############################  
  
FROM kanalfred/centos7:latest  
MAINTAINER Alfred Kan <kanalfred@gmail.com>  
  
# Add Files  
#/etc/cron.d  
ADD container-files/etc /etc  
ADD container-files/config /config  
  
RUN \  
yum -y install \  
samba samba-client samba-common \  
nfs-utils \  
rsync \  
rsnapshot  
# yum clean all && \  
  
RUN \  
# create backup of origal smb.conf  
cp /etc/samba/smb.conf /etc/samba/smb.conf.bak && \  
  
# create unix users  
useradd share && \  
useradd alfred && \  
useradd akimi && \  
  
# add user to share gruop  
usermod -a -G share alfred && \  
usermod -a -G share akimi && \  
  
# import samber users  
pdbedit -i smbpasswd:/config/samba-users.backup && \  
  
# cron.d files permission  
chown -R root:root /etc/cron.d/* && \  
chmod -R 644 /etc/cron.d/* && \  
  
# testing need remove  
mkdir -p /mnt/storage/share && \  
touch /mnt/storage/share/test.txt && \  
chmod 777 -R /mnt  
  
  
# Clean YUM caches to minimise Docker image size  
RUN yum clean all && rm -rf /tmp/yum*  
  
# EXPOSE  
# smb  
expose 445  
expose 139  
expose 135  
# nmb  
expose 137/udp  
expose 138/udp  
#EXPOSE 22  
  
# Run supervisord as demon with option -n  
# supervisord already triggerd from base cetnos7 image  
#CMD dockerize /config/run.sh  
#CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]  

