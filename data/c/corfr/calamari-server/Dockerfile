FROM ubuntu:14.04  
RUN ( \  
apt-get update && \  
apt-get upgrade -y && \  
ln -sf /bin/bash /bin/sh \  
)  
  
RUN ( \  
apt-get update && \  
apt-get --yes --assume-yes install -y python-software-properties software-
properties-common wget \  
)  
  
RUN ( \  
add-apt-repository ppa:saltstack/salt && \  
apt-get update \  
)  
  
RUN ( \  
apt-get install -y psmisc \  
)  
  
ENV BASE_URL http://cor-net.org/wp-content/uploads/2015/02  
ENV BASE_SERVER_FILE calamari-server_1.3-rc-16-g321cd58_amd64.deb  
ENV BASE_CLIENT_FILE calamari-clients_1.2.2-26-gcfbc8bf_all.deb  
  
RUN ( \  
wget --quiet ${BASE_URL}/${BASE_SERVER_FILE} && \  
( dpkg -i ${BASE_SERVER_FILE} || true ) && \  
apt-get --yes --assume-yes install -f && \  
rm ${BASE_SERVER_FILE} \  
)  
  
RUN ( \  
wget --quiet ${BASE_URL}/${BASE_CLIENT_FILE} && \  
( dpkg -i ${BASE_CLIENT_FILE} || true ) && \  
apt-get --yes --assume-yes install -f && \  
rm ${BASE_CLIENT_FILE} \  
)  
  
RUN ( \  
cp $(which python2.7) /opt/calamari/venv/local/bin/python && \  
locale-gen en_US.UTF-8 \  
)  
  
ENV BASE_REPO_FILE calamari-repo-precise.tar.gz  
  
RUN ( \  
wget -O /tmp/${BASE_REPO_FILE} \--quiet ${BASE_URL}/${BASE_REPO_FILE} && \  
cd /opt/calamari/webapp/content && \  
mkdir calamari-minions && \  
cd calamari-minions && \  
tar zxvf /tmp/${BASE_REPO_FILE} \--strip 1 && \  
rm /tmp/${BASE_REPO_FILE} \  
)  
  
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]  
  
EXPOSE 4505 4506 80 2003 2004  
ADD entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
  

