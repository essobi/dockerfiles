FROM pataquets/percona-repo:xenial  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
mariadb-client \  
percona-toolkit \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/  

