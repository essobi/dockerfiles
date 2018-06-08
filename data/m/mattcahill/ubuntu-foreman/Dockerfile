# Build:  
# docker build -t mattcahill/ubuntu-foreman .  
#  
# Run:  
# docker run -d -P --name=ubuntu-foreman -h foreman.example.com
mattcahill/ubuntu-foreman  
#  
# tail log:  
# docker logs -f ubuntu-foreman  
#  
# get port 443 exposed on host  
# docker port ubuntu-foreman 443  
#  
# Used the following projects as reference:  
# riskable/docker-foreman  
# xnaveira/foreman-docker  
#  
# This project used a fork of gbevan/ubuntu-foreman as a starting point  
#  
# Please report issues via github  
  
FROM ubuntu:14.04  
MAINTAINER Matt Cahill  
  
ENV FOREMANVER 1.14  
ENV DEBIAN_FRONTEND noninteractive  
ENV FOREOPTS --foreman-proxy-tftp=false \  
\--foreman-unattended=false \  
\--enable-puppet \  
\--puppet-listen=true \  
\--puppet-show-diff=true \  
\--puppet-server-envs-dir=/etc/puppet/environments  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get -y install ca-certificates wget && \  
wget https://apt.puppetlabs.com/puppetlabs-release-pc1-trusty.deb && \  
dpkg -i puppetlabs-release-pc1-trusty.deb && \  
apt-get install -y wget aptitude htop vim vim-puppet git traceroute dnsutils
&& \  
echo "deb http://deb.theforeman.org/ trusty $FOREMANVER" >
/etc/apt/sources.list.d/foreman.list && \  
echo "deb http://deb.theforeman.org/ plugins $FOREMANVER" >>
/etc/apt/sources.list.d/foreman.list && \  
wget -q http://deb.theforeman.org/pubkey.gpg -O- | apt-key add - && \  
apt-get install -y software-properties-common && \  
apt-add-repository ppa:git-core/ppa -y && \  
apt-get update && \  
apt-get install -y foreman-installer && \  
apt-get install -y git python-pip iotop sysstat krb5-user libkrb5-dev python-
dev python-jinja2 python-yaml python-paramiko python-httplib2 python-six
python-crypto sshpass && \  
apt-add-repository ppa:ansible/ansible && \  
apt-get update && \  
apt-get install -y ansible && \  
pip install 'pywinrm>=0.1.1' && \  
pip install 'kerberos==1.2.2' && \  
echo "set modeline" > /root/.vimrc && \  
echo "export TERM=vt100" >> /root/.bashrc && \  
LANG=en_US.UTF-8 locale-gen --purge en_US.UTF-8 && \  
echo 'LANG="en_US.UTF-8"\nLANGUAGE="en_US:en"\n' > /etc/default/locale && \  
dpkg-reconfigure --frontend=noninteractive locales  
#&& \  
#rm -f /usr/share/foreman-installer/checks/hostname.rb && \  
#export FACTER_fqdn="mjolnir.user.wetafx.co.nz" && \  
#echo "127.1.1.2 mjolnir.user.wetafx.co.nz" >> /etc/hosts && \  
#/usr/sbin/foreman-installer $FOREOPTS; \  
#sed -i -e "s/START=no/START=yes/g" /etc/default/foreman  
  
EXPOSE 443  
EXPOSE 8140  
EXPOSE 8443  
  
CMD ( test ! -f /etc/foreman/.first_run_completed && \  
( echo "FIRST-RUN: Please wait while Foreman is installed and configured...";
\  
/usr/sbin/foreman-installer $FOREOPTS; \  
sed -i -e "s/START=no/START=yes/g" /etc/default/foreman; \  
touch /etc/foreman/.first_run_completed \  
) \  
); \  
/etc/init.d/puppet stop && \  
/etc/init.d/apache2 stop && \  
/etc/init.d/foreman stop && \  
/etc/init.d/postgresql stop && \  
echo "sleeping for postgresql to ensure stopped" && \  
sleep 60 && \  
/etc/init.d/postgresql start && \  
echo "sleeping for postgresql to ensure started" && \  
sleep 60 && \  
/etc/init.d/foreman start && \  
/etc/init.d/apache2 start && \  
/etc/init.d/puppet start && \  
/etc/init.d/foreman-proxy start && \  
/usr/sbin/cron && \  
foreman-rake permissions:reset && \  
/usr/sbin/foreman-rake db:seed && \  
service foreman-proxy restart && \  
tail -f /var/log/foreman/production.log  

