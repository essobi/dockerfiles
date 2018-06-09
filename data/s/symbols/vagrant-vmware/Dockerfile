FROM symbols/vmware  
  
LABEL maintainer="simon@widgit.com"  
  
RUN VERSION=$(wget -O- https://releases.hashicorp.com/vagrant/ | fgrep
'href="/vagrant' | head -1 | sed -r 's/.*([0-9].[0-9].[0-9]).*/\1/') && \  
wget -O /root/vagrant.deb \  
https://releases.hashicorp.com/vagrant/${VERSION}/vagrant_${VERSION}_x86_64.deb
&& \  
dpkg -i /root/vagrant.deb && \  
rm /root/vagrant.deb && \  
apt-get -y update && \  
apt-get -y install rsync sudo kmod && \  
script -e -c "vagrant plugin install vagrant-vmware-workstation" /dev/null &&
\  
apt-get -y clean  
  
COPY vmware-networks /usr/bin/vmware-networks  
  
CMD ["/usr/local/bin/run_vagrant_and_wait.sh"]  
WORKDIR /vagrant  
  

