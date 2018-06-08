# Dockerfile put in https://github.com/dlintw/sh4twbox-build-env  
FROM 32bit/debian:jessie  
MAINTAINER Daniel YC Lin <dlin.tw at gmail>  
# use GMT+8 as localtime  
RUN rm -f /etc/localtime && ln -s /usr/share/zoneinfo/Asia/Taipei
/etc/localtime  
  
# install basic rpm required packages and clean cache  
RUN apt-get update -y \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
cscope \  
curl \  
debfoster \  
deborphan \  
gcc \  
git \  
make \  
python-rpm \  
python-sqlitecachec \  
python-urlgrabber \  
rpm \  
tmux \  
vim \  
&& apt-get clean  
  
# use bash instead of sh  
RUN ln -sf bash /bin/sh  
  
# get newest depdency rpms  
ENV DL http://download.stlinux.com/pub/stlinux/2.4  
RUN curl -o /tmp/deps.rpm $DL/misc/$(curl $DL/misc/ \  
| grep rpm |tail -1|awk -F'>' '{print $3}' \  
| awk -F'<' '{print $1}')  
RUN rpm -ivh --force-debian /tmp/deps.rpm  
  
  
# 2015/04/23 try to get 3.4 headers directly  
## 2015/04/16 workaround for 'install all-sh4-glibc' script  
#RUN curl -o /tmp/ks.rpm $DL/updates/RPMS/host/stlinux24-host-kernel-source-
sh4-2.6.32.61_stm24_0215-215.noarch.rpm  
#RUN curl -o /tmp/fs.rpm $DL/STLinux/host/stlinux24-host-
filesystem-1.0-7.noarch.rpm  
#RUN curl -o /tmp/lkh.rpm $DL/updates/RPMS/sh4/stlinux24-sh4-linux-kernel-
headers-2.6.32.46-48.noarch.rpm  
#RUN rpm -Uvh /tmp/fs.rpm && rpm -Uvh /tmp/ks.rpm && rpm -Uvh /tmp/lkh.rpm  
  
# install & clean cache  
# cache file puts in
/opt/STM/STLinux-2.4/host/var/cache/yum/STLinux_Distribution/packages/  
RUN curl -o /tmp/install $DL/install \  
&& bash -x /tmp/install -u all-sh4-glibc \  
&& /opt/STM/STLinux-2.4/host/bin/stmyum update -y \  
&& /opt/STM/STLinux-2.4/host/bin/stmyum clean dbcache packages \  
&& rm -f /tmp/*rpm  
  
ENV PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/STM/STLinux-2.4/host/bin:/opt/STM/STLinux-2.4/devkit/sh4/bin  

