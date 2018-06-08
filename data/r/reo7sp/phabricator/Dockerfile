FROM debian:jessie  
MAINTAINER Oleg Morozenkov  
  
# install packages  
RUN echo "deb-src http://httpredir.debian.org/debian jessie main" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y sudo ssh git jq supervisor mysql-client uwsgi-plugin-php
php5-cli php5-mysql php5-gd php5-curl php5-json php5-apcu python-pygments && \  
(test `php -r "echo extension_loaded('pcntl');"` -eq "1" || (apt-get source
php5 && cd `ls -1F | grep '^php5-.*/$'`/ext/pcntl && phpize && ./configure &&
make && make install)) && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# download phabricator  
WORKDIR /usr/src  
RUN git clone -b stable --depth 1 https://github.com/phacility/libphutil.git
&& \  
git clone -b stable --depth 1 https://github.com/phacility/arcanist.git && \  
git clone -b stable --depth 1 https://github.com/phacility/phabricator.git &&
\  
rm -rf libphutil/.git arcanist/.git phabricator/.git  
  
# copy additional files  
COPY configs/sshd_config /etc/ssh/sshd_config  
COPY configs/sudoers /etc/sudoers  
COPY configs/supervisor.conf /etc/supervisor.conf  
COPY configs/uwsgi.conf /etc/uwsgi.conf  
COPY scripts/phabricator-ssh-hook.sh /usr/libexec/phabricator-ssh-hook.sh  
COPY scripts/mysql-wait.sh /mysql-wait.sh  
COPY main.sh /main.sh  
RUN mkdir -p /phabricator-
docker/{on_pre_setup,on_post_setup,on_mysql,on_pre_start,on_stop}  
  
# setup phabricator  
WORKDIR /usr/src/phabricator  
  
RUN mkdir -p /var/run/sshd && \  
chmod 755 /usr/libexec/phabricator-ssh-hook.sh  
  
RUN useradd phabricator-vcs && \  
mkdir -p /home/phabricator-vcs && \  
chsh -s /bin/sh phabricator-vcs && \  
sed -i 's/phabricator-vcs:!!*:/phabricator-vcs:NP:/g' /etc/shadow && \  
bin/config set diffusion.ssh-user phabricator-vcs  
  
RUN useradd phabricator-daemon && \  
chsh -s /bin/sh phabricator-daemon && \  
bin/config set phd.user phabricator-daemon  
  
RUN bin/config set phd.taskmasters 1 && \  
bin/config set repository.default-local-path /var/lib/phabricator/repo && \  
bin/config set storage.local-disk.path /var/lib/phabricator/storage && \  
bin/config set pygments.enabled true  
  
# init settings  
VOLUME /var/lib/phabricator  
EXPOSE 22 80  
CMD ["bash", "/main.sh"]  

