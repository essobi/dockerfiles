FROM ubuntu-upstart:14.04  
  
ENV SALT_VERSION=2017.7.1  
  
ADD start.sh /bin/start.sh  
  
RUN apt-get update \  
&& apt-get install -y vim-nox curl \  
&& curl -L
https://repo.saltstack.com/apt/ubuntu/14.04/amd64/archive/${SALT_VERSION}/SALTSTACK-
GPG-KEY.pub | apt-key add \- \  
&& echo "deb
http://repo.saltstack.com/apt/ubuntu/14.04/amd64/archive/${SALT_VERSION}
trusty main" > /etc/apt/sources.list.d/saltstack.list \  
&& apt-get update \  
&& apt-get install -y sudo software-properties-common openntpd apt-transport-
https debian-archive-keyring python-pip \  
&& apt-get install -y salt-minion=${SALT_VERSION}* \  
&& update-rc.d salt-minion defaults 90 90 \  
&& mkdir -p /etc/salt/minion.d \  
&& echo "master: master" > /etc/salt/minion.d/masters.conf \  
&& sed -i -e 's/#hash_type.*/hash_type: sha256/' /etc/salt/minion \  
  
# cleanup  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get -y autoremove \  
&& apt-get clean  
  
ENTRYPOINT ["/bin/start.sh"]  

