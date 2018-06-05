FROM jenkinsci/jenkins  
  
MAINTAINER HighSkillz <webdev@highskillz.com>  
  
ENV DEBIAN_FRONTEND="noninteractive"  
  
USER root  
RUN \  
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
echo "===> Updating TLS certificates..." && \  
apt-get -y install \  
ca-certificates \  
openssl \  
ssl-cert \  
&& \  
\  
echo "===> Adding Python runtime..." && \  
apt-get -y install \  
python \  
python3 \  
\  
build-essential \  
libssl-dev \  
libffi-dev \  
python-dev \  
&& \  
echo "===> Adding usefull packages for devops shell-works..." && \  
apt-get -y install \  
sudo \  
\  
openssh-client \  
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
zip \  
xz-utils \  
\  
git \  
\  
mc \  
screen \  
dos2unix \  
iotop \  
htop \  
atop \  
\  
&& \  
\  
echo "===> Configuring Python and PIP... (debian jessie is not very pip
friendly)" && \  
curl https://bootstrap.pypa.io/get-pip.py| python2 && \  
curl https://bootstrap.pypa.io/get-pip.py| python3 && \  
echo "bootstrapper already installed setuptools and wheel" && \  
\  
rm $(which pip) && \  
ln -s $(which pip2) /usr/local/bin/pip && \  
\  
echo Making sure pip is set to python2 && \  
pip --version | grep "python 2\." && \  
\  
echo "Make sure we can run ansible's docker scripts" && \  
pip3 install --upgrade \  
docker-py \  
docker-compose \  
&& \  
\  
echo "===> Installing Ansible (via pip2)..." && \  
pip2 install --upgrade \  
ansible \  
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
\  
echo "===> Cleaning up ..." && \  
apt-get autoremove --purge -y && \  
apt-get clean -y && \  
rm -rf \  
"${HOME}/.cache" \  
/var/lib/apt/lists/* && \  
\  
echo "..."  
  
RUN \  
ansible-playbook --version | head -n 1 && \  
python3 --version | head -n 1 && \  
pip3 --version | head -n 1 && \  
node --version | head -n 1 && \  
ruby --version | head -n 1 && \  
git --version | head -n 1 && \  
docker-compose --version | head -n 1 && \  
openssl version | head -n 1 && \  
\  
echo "OK!"  
  
USER ${user}  
  
#ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins.sh"]  

