FROM thenewvu/ubuntu-14.04  
MAINTAINER Vu Le "thenewvu@gmail.com"  
# install virtualbox 5.0  
RUN sudo sh -c "echo 'deb http://download.virtualbox.org/virtualbox/debian
'$(lsb_release -cs)' contrib non-free' >
/etc/apt/sources.list.d/virtualbox.list" && \  
wget -q http://download.virtualbox.org/virtualbox/debian/oracle_vbox.asc -O- |
sudo apt-key add - && \  
sudo apt-get update && \  
sudo apt-get install -y virtualbox-5.0  
# clean up  
RUN sudo apt-get clean && \  
sudo rm -rf /var/lib/apt/lists/*  
  
# automatically start virtualbox  
ENTRYPOINT ["/usr/bin/virtualbox"]  

