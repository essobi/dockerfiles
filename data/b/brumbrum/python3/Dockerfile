ARG DOCKER_TAG  
FROM brumbrum/base:$DOCKER_TAG  
MAINTAINER Alessandro Lattao <alessandro.lattao@brumbrum.it>  
  
# Installo i pacchetti base per python  
RUN \  
apt-get -y --no-install-recommends install rsyslog python3-minimal
libpython3-stdlib default-libmysqlclient-dev python3-tk && \  
apt-get -y autoclean && \  
apt-get -y clean && \  
apt-get -y autoremove  
  
# Installo newrelic  
RUN \  
apt-get -y --no-install-recommends install python-pip python-wheel python-
setuptools && \  
pip install newrelic  
  
# Abbiamo aggiunto questa riga perche' Python ha bisogno di una home directory  
# e noi non abbiamo un utente nel container  
ENV HOME=/data  
  
# Configuro rsyslog  
ADD etc/rsyslog.conf /etc/rsyslog.conf  
ADD etc/rsyslog.d/50-default.conf /etc/rsyslog.d/50-default.conf  
  
ADD entrypoint.sh /entrypoint.sh  
RUN ["chmod", "+x", "/entrypoint.sh"]  
ENTRYPOINT ["/entrypoint.sh"]  

