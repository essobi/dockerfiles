FROM centos:centos6  
MAINTAINER John Regan <john@jrjrtech.com>  
  
RUN yum -y --enablerepo=centosplus update && \  
yum -y --enablerepo=centosplus install \  
openssl-devel libevent-devel zlib-devel openldap-devel \  
gcc make tar patch readline-devel expat-devel libidn-devel \  
postgresql-devel sqlite-devel mysql-devel unzip  
  
RUN useradd -r -m -d /opt/metronome -s /sbin/nologin metronome  
ADD as_metronome.sh /opt/metronome/as_metronome.sh  
RUN chmod a+x /opt/metronome/as_metronome.sh  
  
ENV HOME /opt/metronome  
WORKDIR /opt/metronome  
RUN su -l -s /bin/bash metronome /opt/metronome/as_metronome.sh  
  
RUN rm /opt/metronome/as_metronome.sh  
  
RUN yum -y remove openssl-devel libevent-devel zlib-devel openldap-devel \  
gcc cpp patch readline-devel expat-devel libidn-devel \  
postgresql-devel sqlite-devel mysql-devel \  
postgresql mysql cyrus-sasl-devel glibc-devel glibc-headers \  
keyutils-libs-devel libselinux-devel libsepol-devel \  
ncurses-devel perl ppl krb5-devel  
  
ADD metronome.cfg.lua /opt/metronome/etc/metronome.cfg.lua  
RUN mkdir /opt/metronome/var/logs  
  
RUN chown -R metronome /opt/metronome  
  
USER metronome  
ENV PATH $HOME/.luaenv/shims:$HOME/.luaenv/bin:$PATH  
  
VOLUME ["/opt/metronome/etc"]  
VOLUME ["/opt/metronome/var"]  
  
# Client port  
EXPOSE 5222  
# Server-to-server port  
EXPOSE 5269  
# http port  
EXPOSE 5280  
ENTRYPOINT ["metronome"]  

