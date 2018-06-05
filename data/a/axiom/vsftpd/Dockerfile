FROM phusion/baseimage:0.9.21  
CMD ["/sbin/my_init"]  
ENV KILL_PROCESS_TIMEOUT=30  
ENV KILL_ALL_PROCESSES_TIMEOUT=30  
  
MAINTAINER Kyle Wilcox <kyle@axiomdatascience.com>  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG C.UTF-8  
  
RUN apt-get update && apt-get install -y \  
binutils \  
build-essential \  
bzip2 \  
ca-certificates \  
curl \  
libglib2.0-0 \  
libpam-pwdfile \  
libsm6 \  
libxext6 \  
libxrender1 \  
pwgen \  
vsftpd \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir /ftp && \  
mkdir -p -m0755 /var/run/vsftpd/empty && \  
# https://github.com/phusion/baseimage-
docker/pull/392/commits/06b065782df0aa2398e1c9339cbf0b08b1cea720  
sed -i 's#, KILL#% KILL#' /sbin/my_init && \  
chown -R ftp:ftp /ftp && \  
rm -rf /etc/service/cron  
  
COPY ./files /  

