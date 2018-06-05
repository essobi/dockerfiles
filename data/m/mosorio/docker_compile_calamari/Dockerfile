FROM ubuntu:trusty  
  
RUN \  
apt-get install -y wget && \  
echo deb http://ppa.launchpad.net/saltstack/salt/ubuntu `lsb_release -sc` main
| tee /etc/apt/sources.list.d/saltstack.list && \  
wget -q -O-
"http://keyserver.ubuntu.com:11371/pks/lookup?op=get&search=0x4759FA960E27C0A6"
| apt-key add \- && \  
apt-get -y update && \  
apt-get -y install salt-master salt-minion salt-syndic  
  
RUN \  
echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >
/etc/apt/sources.list.d/pgdg.list && \  
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key
add \- && \  
apt-get -y update && apt-get -y upgrade  
  
RUN \  
apt-get install -y curl build-essential openssl libssl-dev apache2
libapache2-mod-wsgi libcairo2 supervisor python-cairo libpq5 postgresql
python-m2crypto python-virtualenv git python-dev swig libzmq-dev g++
postgresql-9.1 postgresql-server-dev-9.1 libcairo2-dev python-pip libpq-dev
ruby debhelper python-mock python-configobj cdbs gem ruby1.9.1 ruby1.9.1-dev
make devscripts software-properties-common python-support  
  
  
RUN \  
cd ~ && \  
git clone https://github.com/joyent/node.git && \  
cd node && \  
git checkout v0.10.10 && \  
./configure && \  
make -j4 && \  
make install  
  
RUN mkdir ~/npm  
  
ADD https://npmjs.org/install.sh /root/npm/install.sh  
RUN bash -x ~/npm/install.sh  
RUN \  
npm install -g bower && \  
npm install -g coffee-script && \  
npm install -g grunt-cli  
  
RUN \  
gem install compass && \  
gem install sass  
  
COPY compile.sh /compile.sh  
RUN chmod +x /compile.sh  
CMD ./compile.sh  

