FROM petervanderdoes/buildenv:trusty  
  
# Set the env variables to non-interactive  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBIAN_PRIORITY critical  
ENV DEBCONF_NOWARNINGS yes  
  
# Upstart and DBus have issues inside docker. Work around it  
#RUN dpkg-divert --local --rename --add /sbin/initctl && ln -s /bin/true
/sbin/initctl  
RUN apt-get update  
  
# Installing the build environment  
RUN apt-get install -y \  
debhelper po-debconf groff-base patch lsb-release libdb-dev libldap2-dev \  
liblmdb-dev libpcre3-dev libmysqlclient-dev libssl-dev libsasl2-dev \  
libpq-dev libcdb-dev dpkg-dev libsqlite3-dev html2text libicu-dev dh-systemd  

