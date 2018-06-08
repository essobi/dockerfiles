FROM ubuntu:14.04  
COPY *.deb /tmp/  
  
RUN echo "deb http://ppa.launchpad.net/git-core/ppa/ubuntu trusty main" >>
/etc/apt/sources.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E1DF1F24 && \  
apt-get update && \  
dpkg -i /tmp/libfontforge1-trusty_amd64.deb || \  
dpkg -i /tmp/python-fontforge-trusty_amd64.deb || \  
apt-get -fy install && \  
apt-get -y install ca-certificates openssl zip git && \  
rm -rf /tmp/*  
  
WORKDIR /data  
  
CMD ["bash"]  

