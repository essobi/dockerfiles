# Build:  
# docker build -t gbevan/vagrant-meanio:0.4.2 .  
#  
# Example Vagrantfile:  
# VAGRANTFILE_API_VERSION = "2"  
# Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|  
# config.vm.define "slm.io", primary: true do |slmio|  
# slmio.vm.provision "shell", inline: '/usr/bin/mongod --config
/etc/mongod.conf --fork'  
# slmio.vm.synced_folder "src/", "/home/vagrant/appserver/packages/custom"  
# slmio.vm.provider "docker" do |d|  
# d.image = "gbevan/vagrant-meanio:latest"  
# d.has_ssh = true  
# end  
# end  
# end  
#  
# Run:  
# vagrant up \--provider=docker  
#  
# resolve dns issues:  
# /etc/conf/docker  
# DOCKER_OPTS="--dns ip_1 --dns ip_2"  
#  
  
FROM ubuntu:14.04  
MAINTAINER Graham Bevan "graham.bevan@ntlworld.com"  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG=C  
ENV LC_ALL=C  
  
ADD fix-bower.sh /  
ADD start-image.sh /  
  
# Dependencies + Vagrant  
RUN \  
apt-get -yq update && \  
apt-get install -y software-properties-common && \  
apt-add-repository ppa:git-core/ppa -y && \  
apt-get -yq update && \  
apt-get dist-upgrade -yq && \  
apt-get install -yqq wget aptitude htop vim vim-puppet git traceroute dnsutils
\  
curl ssh sudo psmisc gcc make build-essential libfreetype6 libfontconfig \  
augeas-tools tree tcpdump && \  
mkdir /var/run/sshd && \  
sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config && \  
sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config && \  
useradd --create-home -s /bin/bash vagrant && \  
mkdir -p /home/vagrant/.ssh && \  
echo "ssh-rsa
AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoPkcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0zQPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbUvxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCzRdK8jlqm8tehUc9c9WhQ==
vagrant insecure public key" > /home/vagrant/.ssh/authorized_keys && \  
chown -R vagrant: /home/vagrant/.ssh && \  
echo -n 'vagrant:vagrant' | chpasswd && \  
su - vagrant -c "touch /home/vagrant/.hushlogin" && \  
mkdir -p /etc/sudoers.d && \  
echo "vagrant ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/vagrant && \  
chmod 0440 /etc/sudoers.d/vagrant && \  
echo "set modeline" > /etc/vim/vimrc.local && \  
echo "export TERM=vt100\nexport LANG=C\nexport LC_ALL=C" >
/etc/profile.d/dockenv.sh && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv EA312927 && \  
apt-get clean && \  
echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2
multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list && \  
apt-get -yq update && \  
apt-get install -yqq mongodb-org && \  
curl -sL https://deb.nodesource.com/setup_4.x | sudo bash - && \  
apt-get -yq update && \  
apt-get install -yqq nodejs && \  
apt-get clean && \  
npm install -g node-gyp && \  
npm install -g grunt-cli && \  
npm install -g gulp && \  
npm install -g karma-cli && \  
npm install -g mocha && \  
npm install -g bower && \  
npm install -g mean-cli@0.9.21 && \  
npm cache clean && \  
/usr/bin/mongod --config /etc/mongod.conf \--fork --smallfiles && \  
echo "export MONGOOSE_DISABLE_STABILITY_WARNING=1" >> ~/.bashrc && \  
export MONGOOSE_DISABLE_STABILITY_WARNING=1 && \  
su - vagrant -c'mkdir -p .npm; echo -e "\n\n \n" | mean init --branch v0.4.2
appserver && cd appserver && sed -i
"s/\\\\(mongoose.:.*\\\\)^3\\\\.8\\\\.8\\\\(.*\\\\)/\13.8\2/" package.json &&
npm install && /fix-bower.sh && bower --config.interactive=false install &&
mkdir -p packages/contrib && git clone --depth 1
https://github.com/gbevan/mean-admin.git packages/contrib/mean-admin && cd
packages/contrib/mean-admin && npm install && bower install && cd ~/appserver
&& npm cache clean; bower cache clean' && \  
perl -e 'local $/=undef; open(GR,"</home/vagrant/appserver/Gruntfile.js");
binmode GR; $F=<GR>; $F=~s/(mochaTest: {.\s*options: {)/$1\n timeout:
20000,/ms; open(NG, ">/home/vagrant/appserver/Gruntfile.js"); print NG $F' &&
\  
su - vagrant -c'cd appserver && grunt test' && \  
killall mongod && sleep 10 && (killall -9 mongod 2>/dev/null || true) && sleep
5 && \  
rm -rf /var/lib/mongodb/* /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
  
#CMD ["/usr/sbin/sshd", "-D", "-e"]  
ENTRYPOINT ["/bin/bash", "/start-image.sh"]  
  
EXPOSE 22 3000  

