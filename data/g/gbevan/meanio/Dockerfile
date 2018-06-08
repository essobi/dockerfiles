# Build:  
# docker build -t gbevan/meanio:0.4.2 .  
#  
# Run:  
#  
  
FROM ubuntu:14.04  
MAINTAINER Graham Bevan "graham.bevan@ntlworld.com"  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG=C  
ENV LC_ALL=C  
  
ADD fix-bower.sh /  
ADD start-image.sh /  
  
# Dependencies  
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
useradd --create-home -s /bin/bash mean && \  
su \- mean -c "mkdir -p .ssh; chmod 700 .ssh" && \  
echo -n "mean:`openssl rand -base64 15`" | chpasswd && \  
su \- mean -c "touch .hushlogin" && \  
mkdir -p /etc/sudoers.d && \  
echo "mean ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/mean && \  
chmod 0440 /etc/sudoers.d/mean && \  
echo "set modeline" > /etc/vim/vimrc.local && \  
echo "export TERM=vt100\nexport LANG=C\nexport LC_ALL=C" >
/etc/profile.d/dockenv.sh && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927 && \  
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
npm install -g forever && \  
npm cache clean && \  
/usr/bin/mongod --config /etc/mongod.conf \--fork --smallfiles && \  
echo "export MONGOOSE_DISABLE_STABILITY_WARNING=1" >> ~/.bashrc && \  
export MONGOOSE_DISABLE_STABILITY_WARNING=1 && \  
su \- mean -c'mkdir -p .npm; echo -e "\n\n \n" | mean init --branch v0.4.2
appserver && cd appserver && sed -i
"s/\\\\(mongoose.:.*\\\\)^3\\\\.8\\\\.8\\\\(.*\\\\)/\13.8\2/" package.json &&
npm install && /fix-bower.sh && bower --config.interactive=false install &&
mkdir -p packages/contrib && git clone --depth 1
https://github.com/gbevan/mean-admin.git packages/contrib/mean-admin && cd
packages/contrib/mean-admin && npm install && bower install && cd ~/appserver
&& npm cache clean; bower cache clean' && \  
perl -e 'local $/=undef; open(GR,"</home/mean/appserver/Gruntfile.js");
binmode GR; $F=<GR>; $F=~s/(mochaTest: {.\s*options: {)/$1\n timeout:
20000,/ms; open(NG, ">/home/mean/appserver/Gruntfile.js"); print NG $F' && \  
su \- mean -c'cd appserver && grunt test' && \  
(/usr/bin/mongod --shutdown --config /etc/mongod.conf &) && \  
sleep 5 && \  
(killall mongod 2>/dev/null || true) && sleep 10 && (killall -9 mongod
2>/dev/null || true) && sleep 5 && \  
rm -rf /var/lib/mongodb/* /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
  
ENTRYPOINT ["/bin/bash", "/start-image.sh"]  
  
EXPOSE 3000  

