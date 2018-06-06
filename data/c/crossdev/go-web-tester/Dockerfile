FROM golang  
MAINTAINER Roman Saveljev <roman.saveljev@haltian.com>  
  
RUN \  
export DEBIAN_FRONTEND=noninteractive && \  
apt-key update && \  
apt-get -y update && \  
apt-get install -y curl psmisc sudo  
  
RUN \  
curl -L https://github.com/sstephenson/bats/archive/v0.4.0.tar.gz | tar xzv -C
/tmp && \  
/tmp/bats-0.4.0/install.sh /usr/local && \  
rm -rf /tmp/bats-0.4.0  
  
RUN \  
echo "Defaults:root !env_reset" >/etc/sudoers.d/tester_extra && \  
echo "Defaults:root !secure_path" >/etc/sudoers.d/tester_extra && \  
echo "nobody ALL=(ALL) NOPASSWD:ALL" >>/etc/sudoers.d/tester_extra  
  
RUN \  
go get github.com/tools/godep  

