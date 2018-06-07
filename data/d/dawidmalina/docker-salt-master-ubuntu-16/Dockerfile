FROM ubuntu:16.04  
  
ENV SALT_VERSION=2017.7.1  
  
ADD start.sh /bin/start.sh  
  
RUN apt-get update \  
&& apt-get install -y vim-nox curl \  
&& curl -L
https://repo.saltstack.com/apt/ubuntu/16.04/amd64/archive/${SALT_VERSION}/SALTSTACK-
GPG-KEY.pub | apt-key add \- \  
&& echo "deb
http://repo.saltstack.com/apt/ubuntu/16.04/amd64/archive/${SALT_VERSION}
xenial main" > /etc/apt/sources.list.d/saltstack.list \  
&& apt-get update \  
&& apt-get install -y libdbus-1-3 libnih-dbus1 sudo software-properties-common
python-pip kmod iputils-ping apt-transport-https debian-archive-keyring \  
&& apt-get install -y salt-minion=${SALT_VERSION}* \  
&& apt-get install -y salt-master=${SALT_VERSION}* salt-api=${SALT_VERSION}*
salt-ssh=${SALT_VERSION}* \  
&& pip install \--upgrade pip \  
&& pip install cherrypy==3.2.2 \  
&& mkdir -p /etc/salt/minion.d \  
&& echo "master: master" > /etc/salt/minion.d/masters.conf \  
&& sed -i -e 's/#hash_type.*/hash_type: sha256/' /etc/salt/minion \  
  
# remove libexpat1-dev  
&& apt-get -y purge libexpat1-dev \  
  
# salt-api configuration  
&& sed -i -e 's/#default_include.*/default_include: master.d\/\\*.conf/'
/etc/salt/master \  
&& sed -i -e 's/#user.*/user: root/' /etc/salt/master \  
&& sed -i -e 's/#hash_type.*/hash_type: sha256/' /etc/salt/master \  
&& echo "auto_accept: True" > /etc/salt/master.d/auto_sign.conf \  
&& echo "interface: 0.0.0.0\n\nfile_roots:\n base:\n -
/srv/salt/state\n\npillar_roots:\n base:\n - /srv/salt/pillar\n" >
/etc/salt/master.d/backends.conf \  
  
# add salt-api  
&& echo "rest_cherrypy:\n port: 8000\n host: 0.0.0.0\n disable_ssl: true\n" >
/etc/salt/master.d/salt-api.conf \  
&& echo "external_auth:\n pam:\n api:\n - .*\n - '@runner'\n - '@wheel'\n" >>
/etc/salt/master.d/salt-api.conf \  
&& useradd -m -p api123 -s /bin/bash api \  
  
# fix for getty consume 100% cpu  
&& systemctl disable getty@tty1.service \  
  
# fix for systemd  
&& systemctl enable salt-master \  
&& systemctl enable salt-minion \  
  
# fix missing resolvconf  
&& cd /tmp \  
&& apt-get download resolvconf \  
&& dpkg \--unpack resolvconf_*_all.deb \  
&& rm /var/lib/dpkg/info/resolvconf.postinst \  
&& dpkg \--configure resolvconf \  
&& apt-get install -yf \  
&& apt-mark hold resolvconf \  
  
# cleanup  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get -y autoremove \  
&& apt-get clean  
  
EXPOSE 4505 4506  
  
ENTRYPOINT ["/bin/start.sh"]  

