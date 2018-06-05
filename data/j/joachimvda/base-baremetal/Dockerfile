### joachimvda/base-baremetal  
# Yes, we are running LTS  
from ubuntu:12.04  
  
# Joachim is in charge  
maintainer Joachim Van der Auwera <joachim@progs.be>  
  
# Opening-up the repo to universe as well  
run echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
  
# Check that we are up to date  
run apt-get update  
run apt-get -y upgrade  
  
# and keep us up-to-date  
run apt-get -y install unattended-upgrades  
  
# and please give me joe  
run apt-get -y install joe  
  
# Keep upstart from complaining  
run dpkg-divert --local --rename --add /sbin/initctl  
run ln -s /bin/true /sbin/initctl  
  
# Useful base packages  
run apt-get -y install supervisor  
run mkdir -p /var/log/supervisor  
run locale-gen en_US en_US.UTF-8  
#add supervisord-bare.conf /etc/supervisor/conf.d/  
# Change root password  
#run echo 'root:XXXXXXXXX' | chpasswd  
  
cmd ["/usr/bin/supervisord", "-n"]  

