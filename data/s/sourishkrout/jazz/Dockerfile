FROM ubuntu:precise  
  
MAINTAINER Sebastian Tiedtke <sebastiantiedtke@gmail.com> version: 0.1  
  
RUN \  
echo "deb http://archive.ubuntu.com/ubuntu precise universe" >>
/etc/apt/sources.list ;\  
echo "deb http://ppa.launchpad.net/chris-lea/node.js/ubuntu precise main" >>
/etc/apt/sources.list ;\  
apt-get update ;\  
apt-get install -y --force-yes libmysqlclient-dev python-dev python-pip nodejs
;\  
pip install -U virtualenv ;\  
npm install -g bower grunt-cli ;\  
# END RUN  

