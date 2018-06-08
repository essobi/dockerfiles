##################################################################################  
##  
## VERSION : 0.0.5  
## DATE : 31May2016  
##  
## USAGE : Dockerfile to build a super lightweight container to run uTorrent
in Linux with mounted volumes for data storage  
## Ref [1] : https://github.com/miztiik/cloudera-On-Docker/blob/master/docker-
image-build/uTor/centos/Dockerfile  
## Ref [2] : https://github.com/jeanblanchard/docker-alpine-
glibc/blob/master/Dockerfile  
##################################################################################  
  
FROM alpine:latest  
MAINTAINER Mystique  
  
# Install the support packages  
# - Download & Install glibc (needed for utserver)  
# - Setup sym links, remove un-used packages, clean cachce, Setup up entry
points  
RUN apk add --update curl libgcc openssl && \  
curl -o glibc-2.21-r2.apk "https://circle-artifacts.com/gh/andyshinn/alpine-
pkg-glibc/6/artifacts/0/home/ubuntu/alpine-pkg-
glibc/packages/x86_64/glibc-2.21-r2.apk" && \  
apk add --allow-untrusted glibc-2.21-r2.apk && \  
curl -o glibc-bin-2.21-r2.apk "https://circle-
artifacts.com/gh/andyshinn/alpine-pkg-glibc/6/artifacts/0/home/ubuntu/alpine-
pkg-glibc/packages/x86_64/glibc-bin-2.21-r2.apk" && \  
apk add --allow-untrusted glibc-bin-2.21-r2.apk && \  
/usr/glibc/usr/bin/ldconfig /lib /usr/glibc/usr/lib && \  
echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf && \  
apk del curl && \  
rm -rf glibc-2.21-r2.apk glibc-bin-2.21-r2.apk /var/cache/apk/* && \  
mkdir -p /opt/utorrent;  
  
# Install necessary packages & Create sym link for libssl because the CentOS 6
has newer version than what uTorrent requires  
RUN ln -s /usr/lib/libssl.so.1.0.0 /usr/lib/libssl.so.0.9.8 && \  
ln -s /usr/lib/libcrypto.so.1.0.0 /usr/lib/libcrypto.so.0.9.8  
  
# Expose external connectivity port & the web interface  
EXPOSE 2891 8085  
  
# Setting up the entry point to allow for graceful exit when the container is
stopped  
ENTRYPOINT ["/opt/utorrent/utserver" , "-settingspath" , "/opt/utorrent/" ,
"-configfile"]  
CMD ["/opt/utorrent/utserver.conf", "&"]  
  

