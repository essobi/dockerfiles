# adapted from [ williamyeh/ansible:ubuntu14.04-onbuild ]  
# "ONBUILD version" because:  
# - updates some SSL stuff everytime is used in another image  
# - copies . to /tmp/ops  
#  
# added some improvements from [ https://github.com/timhaak/docker-base ]  
  
FROM ubuntu:14.04  
  
MAINTAINER HighSkillz <webdev@highskillz.com>  
  
ENV DEBIAN_FRONTEND="noninteractive"  
ENV PIP__ANSIBLE="ansible~=2.2"  
  
RUN \  
echo "===> Enabling Multiverse..." && \  
sed -i "/^# deb.*multiverse/ s/^# //" /etc/apt/sources.list && \  
\  
echo "===> Speeding up apt and dpkg..." && \  
echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup && \  
echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache && \  
\  
echo "===> Initial packages update" && \  
apt-get update && \  
apt-get -y install \  
apt-transport-https \  
lsb-release \  
software-properties-common \  
&& \  
\  
echo "===> Adding PPAs..." && \  
echo OFF: add-apt-repository -y ppa:ansible/ansible && \  
add-apt-repository -y ppa:brightbox/ruby-ng && \  
apt-get update && \  
\  
echo "===> Updating TLS certificates..." && \  
apt-get -y install \  
ca-certificates \  
openssl \  
ssl-cert \  
&& \  
\  
echo "===> Upgrading distribution..." && \  
apt-get -y dist-upgrade && \  
\  
echo "===> Adding Python runtime..." && \  
apt-get -y install \  
python python-pip \  
python3 python3-pip \  
&& \  
echo "===> Adding usefull packages for devops shell-works..." && \  
apt-get -y install \  
openssh-client \  
inetutils-ping \  
rsync \  
\  
bash \  
less \  
nano \  
\  
curl \  
wget \  
\  
realpath \  
virt-what \  
cpu-checker \  
zip \  
xz-utils \  
\  
git \  
\  
mc \  
mosh \  
screen \  
dos2unix \  
deborphan \  
\  
lsscsi \  
\  
iotop \  
htop \  
atop \  
sysstat \  
dstat \  
iftop \  
ifstat \  
bmon \  
\  
tcptrack \  
iptraf \  
nethogs \  
lsof \  
procinfo \  
util-linux \  
mtr \  
\  
postgresql-client \  
mysql-client \  
\  
&& \  
\  
echo "===> Configuring Python and PIP..." && \  
pip3 install --upgrade pip setuptools wheel && \  
pip2 install --upgrade pip setuptools wheel && \  
rm $(which pip) && \  
ln -s $(which pip2) /usr/local/bin/pip && \  
\  
echo Making sure pip is set to python2 && \  
pip --version | grep "python 2\\." && \  
\  
echo "===> Installing Ansible (via pip, to have control of installed
version)..." && \  
apt-get -y install \  
libssl-dev libffi-dev \  
python-dev \  
&& \  
\  
pip install --upgrade \  
${PIP__ANSIBLE} \  
&& \  
\  
echo "Make sure we can run ansible's docker scripts" && \  
pip3 install --upgrade \  
docker-py \  
docker-compose \  
ansible-container \  
&& \  
\  
echo "===> Installing NodeJS 6.x..." && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get -y install \  
nodejs \  
&& \  
\  
echo "===> Adding Ruby 2.x..." && \  
apt-get -y install \  
ruby \  
&& \  
echo "===> Adding docker-ssh-exec..." && \  
curl -L https://github.com/mdsol/docker-ssh-
exec/releases/download/v0.5.2/docker-ssh-exec_0.5.2_linux_amd64.tar.gz | \  
tar -xz --strip-components=1 -C /usr/local/bin \  
&& \  
\  
echo "===> Cleaning up ..." && \  
apt-get autoremove --purge -y && \  
apt-get clean -y && \  
rm -rf \  
"${HOME}/.cache" \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
&& \  
\  
echo "OK!"  
# default command: display Ansible version  
CMD \  
ansible-playbook --version | head -n 1 && \  
python --version | head -n 1 && \  
python3 --version | head -n 1 && \  
pip --version | head -n 1 && \  
pip3 --version | head -n 1 && \  
node --version | head -n 1 && \  
ruby --version | head -n 1 && \  
git --version | head -n 1 && \  
docker-compose --version | head -n 1 && \  
openssl version | head -n 1  

