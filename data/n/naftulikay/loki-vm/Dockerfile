FROM naftulikay/xenial-vm  
  
# install repository and key  
RUN apt-key adv --keyserver pool.sks-keyservers.net --recv-keys
6C8769CEDC20F5E66C3B7D37BF36996C4E1F8A59  
COPY files/elementary.list /etc/apt/sources.list.d/  
  
# reconfigure os-release to report accurately  
COPY files/os-release /etc/os-release  
# reconfigure lsb-release to report accurately  
COPY files/lsb-release /etc/lsb-release  
  
# install the elementary-desktop metapackage  
RUN apt-get update >/dev/null \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y elementary-desktop \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean  
  
ENTRYPOINT ["/lib/systemd/systemd"]  

