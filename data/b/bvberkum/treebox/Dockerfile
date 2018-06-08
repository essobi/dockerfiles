  
# Latest is 0.10.0  
FROM phusion/baseimage:latest  
  
MAINTAINER B. van Berkum <dev@dotmpe.com>  
  
LABEL \  
description="Lots of dev tooling and a user setup" \  
urls.hub=https://hub.docker.com/r/bvberkum/treebox \  
urls.repo=https://github.com/bvberkum/x-docker  
  
# Setup package manager  
RUN \  
DEBIAN_FRONTEND=noninteractive; RUNLEVEL=1; \  
apt-get update -qqy && \  
apt-get upgrade -y -o Dpkg::Options::="--force-confold" && \  
apt-get install -qqy --allow-downgrades \  
bash build-essential curl dash elinks git graphviz imagemagick \  
figlet update-motd \  
make man moreutils netcat nodejs npm pandoc php-cli posh \  
python python-dev python-tox python-yaml \  
realpath ruby-full rubygems socat sqlite3 ssh sudo tmux tree uuid-runtime \  
vim git-annex \  
software-properties-common \  
autoconf libtool && \  
curl -s \  
https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | \  
bash && \  
apt-get update -qqy && \  
apt-get install -qqy git-lfs && \  
rm -rf /var/cache/apt/*  
  
ARG node_version=lts  
  
RUN \  
npm install --quiet -g npm && \  
npm cache clean -f && \  
npm install --quiet -g n && \  
n $node_version && \  
chmod g+rw /usr/local/* /usr/local/lib/node_modules && \  
chgrp staff /usr/local/* /usr/local/lib/node_modules && \  
version="$(cd /usr/local/n/versions/node/; echo * | tr ' ' '\n' | sort -rn |
head -n 1)"; \  
{ test -e /usr/bin/node || \  
ln -sf /usr/local/n/versions/node/$version/bin/node /usr/bin/node ; }  
  
RUN \  
cd /tmp/ && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python
get-pip.py && \  
pip install --quiet \  
setuptools PyYAML zope.interface zope.component objectpath docutils && \  
for b in rst2html rst2xml rst2pxml; do \  
ln -s /usr/local/bin/$b.py /usr/local/bin/$b; done  
  
RUN \  
npm install --quiet -g coffee-script pm2 grunt grunt-cli webpack && \  
gem install --quiet sass  
  
# TODO: fix pm2 fsevents  
# TODO: accumulating current dev deps above. should split up into multiple
bases and derivatives, one big one perhaps  
# Replace /etc/profile with local on PATH, because profile.d/ssh-env does not  
# seem to do it.  
RUN \  
echo 'export PATH=$PATH:/usr/local/bin' > /etc/profile.d/ssh-environment; \  
mv /etc/profile /tmp/profile; \  
{ echo 'export PATH=$PATH:/usr/local/bin'; \  
cat /tmp/profile; \  
} >/etc/profile  
  
RUN { \  
echo ; \  
echo "if test -e ~/.bashrc ; then source ~/.bashrc ; fi "; \  
} >> /etc/bash.bashrc  
  
# Fancy up SSH  
RUN \  
figlet Treebox > /etc/ssh/banner && \  
echo "Banner /etc/ssh/banner" >> /etc/ssh/sshd_config  
  
# TODO: And login (update-motd)  
#RUN \  
# echo "" >> /etc/my_init.d  
# Setup user and prepare for ssh, sudo  
ARG username=treebox  
  
RUN \  
addgroup supergroup && \  
touch /etc/sudoers.d/treebox && { \  
echo "$username ALL=NOPASSWD:/usr/sbin/service *"; \  
echo "$username ALL=(www-data) NOPASSWD:ALL"; \  
} > /etc/sudoers.d/treebox  
  
# FIXME: I don't think I should need or want to create a system-user, however  
# usermod does not find the added user otherwise.  
RUN \  
adduser --system --home /home/$username \--shell /bin/bash --group $username
&& \  
usermod $username -a -G sudo,staff,supergroup,ssh && \  
\  
mkdir -vp /home/$username/project && \  
git clone https://github.com/basherpm/basher.git /home/$username/.basher && \  
( echo 'export PATH="$HOME/.basher/bin:$PATH"' >>
/home/$username/.bash_profile ) && \  
\  
chown -R $username:$username /home/$username/  
  
RUN \  
chgrp supergroup /etc/container_environment && \  
chmod -R g+rx /etc/container_environment  
  
RUN locale-gen en_US.UTF-8  
  
# Fancy up env  
ENV TREEBOX_USER=$username \  
TREEBOX_BUILD_ID=$BUILD_CODE \  
TREEBOX_IMAGE=$BUILD_IMAGE \  
TREEBOX_TAG=$DOCKER_TAG \  
TREEBOX_SCM=$SCM_TYPE \  
TREEBOX_SCM_BRANCH=$GIT_BRANCH \  
TREEBOX_SCM_COMMIT=$GIT_COMMIT \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US:en \  
LC_ALL=en_US.UTF-8  
USER $username  
  
ENV LANG=en_US.UTF-8  
# Id: x-docker/0.0.2-dev  

