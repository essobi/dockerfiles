##################################################################################  
##  
## VERSION : 0.0.4  
## DATE : 26Aug2015  
##  
## USAGE : Dockerfile to build GUI applications within Docker, starting with
firefox and uTorrent  
## Ref [1] : http://tutorialforlinux.com/2014/07/20/how-to-install-utorrent-
bittorrent-client-on-centos-6-x-32-64bit-linux-easy-guide/  
## Ref [2] : http://www.ezylinux.com/en/how-to-install-utorrent-on-centos-6/  
##################################################################################  
  
FROM centos:6.6  
MAINTAINER mystique <miztiik@gmail.com>  
  
# Install necessary packages & Create sym link for libssl because the CentOS 6
has newer version than what uTorrent requires  
RUN yum -y install wget tar glibc libgcc openssl098e; \  
ln -s /usr/lib64/libssl.so.0.9.8e /usr/lib64/libssl.so.0.9.8; \  
ln -s /usr/lib64/libcrypto.so.0.9.8e /usr/lib64/libcrypto.so.0.9.8 && \  
yum clean all  
  
# Download utorrent and install install it  
RUN mkdir -p /opt/utorrent && cd /opt/utorrent; \  
wget http://download.utorrent.com/linux/utorrent-
server-3.0-ubuntu-10.10-27079.x64.tar.gz && \  
tar zxvf /opt/utorrent/utorrent-server-3.0-ubuntu-10.10-27079.x64.tar.gz && \  
mv /opt/utorrent/utorrent-server-v3_0/* /opt/utorrent/ && \  
rm -rf /opt/utorrent/utorrent-server-3.0-ubuntu-10.10-27079.x64.tar.gz
/opt/utorrent/utorrent-server-v3_0  
  
# Add the configuration file  
ADD utserver.conf /opt/utorrent/utserver.conf  
  
# Expose external connectivity port & the web interface  
EXPOSE 2891 8085  
  
# Setting up the entry point to allow for graceful exit when the container is
stopped  
ENTRYPOINT ["/opt/utorrent/utserver" , "-settingspath" , "/opt/utorrent/" ,
"-configfile"]  
CMD ["/opt/utorrent/utserver.conf", "&"]  
  
  
# Connect to gui @ localhost:8085/gui  
# user name: admin  
# pass:  
  
## Usage : docker run -dti --name rotnode -p 28920:2891 -p 28921:8085 -v
/media/sf_dockerRepos:/media/sf_dockerRepos mystique/rotnodes:v2  

