# VERSION 0.2  
#  
# Build CoprHDDevKit  
FROM opensuse:13.2  
MAINTAINER "Victor da Costa" <victorockeiro@gmail.com>  
  
ENV VERSION master  
WORKDIR /build  
  
## Clean-up Systemd  
RUN ( for i in /lib/systemd/system/sysinit.target.wants/*; do \  
[ $i == systemd-tmpfiles-setup.service ] || rm -f $i; \  
done; \  
rm -f /lib/systemd/system/multi-user.target.wants/*; \  
rm -f /etc/systemd/system/*.wants/*; \  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*; \  
rm -f /lib/systemd/system/anaconda.target.wants/* )  
  
ADD https://raw.githubusercontent.com/CoprHD/coprhd-
controller/master/packaging/appliance-
images/openSUSE/13.2/CoprHDDevKit/configure.sh /tmp/configure.sh  
RUN chmod +x /tmp/configure.sh && \  
/tmp/configure.sh installRepositories && \  
/tmp/configure.sh installPackages && \  
/tmp/configure.sh installStorageOS && \  
/tmp/configure.sh installJava && \  
/tmp/configure.sh installNetworkConfigurationFile && \  
rm -rf /tmp/*  
  
CMD ["/sbin/init"]  

