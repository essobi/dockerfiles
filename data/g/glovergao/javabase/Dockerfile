FROM debian:jessie  
MAINTAINER glover.gao@grapecity.com  
  
USER root  
  
# Never prompts the user for choices on installation/configuration of packages  
ENV DEBIAN_FRONTEND noninteractive  
# No dialog on apt-get update  
ENV TERM linux  
# Work around initramfs-tools running on kernel 'upgrade':
<http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=594189>  
ENV INITRD No  
  
# Define en_US.  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV LC_CTYPE en_US.UTF-8  
ENV LC_MESSAGES en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# Define base oracle java install path  
ENV JAVA_BASE /opt/oracle/java  
  
# Install curl, locales, apt-utils and gosu  
# create en_US.UTF-8  
# update distribution package  
RUN apt-get update -qq && \  
apt-get install -y apt-utils curl locales && \  
sed -i 's/^# en_US.UTF-8 UTF-8$/en_US.UTF-8 UTF-8/g' /etc/locale.gen &&
locale-gen && \  
update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 && \  
apt-get update -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /var/lib/apt/lists/* /tmp/* /var/tmp/*
/var/cache/*  
  
# Define default workdir  
WORKDIR /root  
  
# Define default command.  
CMD [ "/bin/bash", "-l"]

