FROM debian:jessie  
MAINTAINER Philippe Pepiot <phil@philpep.org>  
  
RUN printf 'APT::Install-Recommends "0";\nAPT::Install-Suggests "0";\n' >
/etc/apt/apt.conf.d/no-recommands  
  
RUN apt-get -qqy update && apt-get -y install \  
apt-transport-https ca-certificates curl lxc iptables \  
openjdk-7-jre-headless sudo ssh locales build-essential git \  
redis-server rsync wget python python-dev python3-dev \  
python-pip python3-pip mercurial \  
php5-cli php5-curl php5-json  
  
# Locales  
RUN echo "LANG=en_US.UTF-8" > /etc/default/locale && \  
echo "LANGUAGE=en_US:en" >> /etc/default/locale && \  
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \  
locale-gen && \  
update-locale  
  
# Python  
RUN python -m pip install -U pip && \  
python3 -m pip install -U pip && \  
python -m pip install -U virtualenv tox && \  
python3 -m pip install -U virtualenv && \  
rm -rf /root/.cache/pip  
  
# Docker  
ADD https://raw.githubusercontent.com/jpetazzo/dind/master/wrapdocker
/usr/local/bin/wrapdocker  
RUN echo "deb https://apt.dockerproject.org/repo debian-jessie main" >
/etc/apt/sources.list.d/docker.list && \  
wget https://apt.dockerproject.org/gpg -O - | apt-key add - && \  
apt-get -qqy update && apt-get -y install docker-engine aufs-tools && \  
chmod +x /usr/local/bin/wrapdocker  
  
# PostgreSQL  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" >
/etc/apt/sources.list.d/pgdg.list && \  
wget -q -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add
- && \  
apt-get -qqy update && apt-get -y install \  
postgresql-9.4 postgresql-server-dev-9.4 postgresql-contrib-9.4 && \  
service postgresql start && \  
su - postgres -c 'createuser -s jenkins; createdb -O jenkins jenkins'  
  
# Phabricator cli tools  
RUN mkdir -p /usr/local/share/phabricator && \  
git clone -b master https://github.com/phacility/libphutil.git
/usr/local/share/phabricator/libphutil && \  
git clone -b master https://github.com/phacility/arcanist.git
/usr/local/share/phabricator/arcanist && \  
ln -fsn /usr/local/share/phabricator/arcanist/bin/arc /usr/local/bin/arc  
  
# Jenkins user  
RUN useradd -m -s /bin/bash jenkins && \  
mkdir -p /home/jenkins/workspace && \  
chown jenkins:jenkins /home/jenkins/workspace && \  
mkdir -p /var/lib/docker/jenkins && \  
mkdir -p /home/jenkins/.ssh && \  
chown jenkins:jenkins /home/jenkins/.ssh && \  
mkdir -p /home/jenkins/.pip && \  
chown jenkins:jenkins /home/jenkins/.pip && \  
echo jenkins:jenkins | chpasswd && \  
adduser jenkins docker && \  
echo "jenkins ALL=(root) NOPASSWD: ALL" > /etc/sudoers.d/jenkins && \  
chmod 440 /etc/sudoers.d/jenkins  
  
# Tmpfs: we divert because some old docker plugin version have /usr/sbin/sshd
hard-coded  
RUN mkdir -p /var/run/sshd && \  
dpkg-divert --add --rename --divert /usr/sbin/sshd.real /usr/sbin/sshd  
ADD wrapsshd /usr/sbin/sshd  
RUN chmod +x /usr/sbin/sshd  
  
EXPOSE 22  
VOLUME /var/lib/docker  
CMD ["/usr/sbin/sshd", "-D"]  

