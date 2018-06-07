FROM centos:centos6  
MAINTAINER kvaps <kvapss@gmail.com>  
ENV REFRESHED_AT 2016-01-03  
RUN yum -y update  
RUN yum -y install epel-release  
  
# Install additional soft  
RUN yum -y install supervisor fail2ban dhclient lua-ldap mercurial tar rsyslog
dhclient  
  
# Install build-essentials and lua-modules  
RUN yum -y install gcc lua-devel openssl-devel libidn-devel lua-expat lua-
socket lua-filesystem lua-sec lua-dbi lua-event  
  
ENV LUACPATH="/usr/lib64/lua/5.1"  
ENV LIBDIR="-L/usr/lib64"  
# Install lua-zlib module  
RUN curl https://codeload.github.com/brimworks/lua-zlib/tar.gz/v0.4 | tar xzv
-C /usr/src/  
WORKDIR /usr/src/lua-zlib-0.4/  
RUN make linux  
RUN make install  
  
# Install lua-bitop module  
RUN curl http://bitop.luajit.org/download/LuaBitOp-1.0.2.tar.gz | tar xzv -C
/usr/src/  
WORKDIR /usr/src/LuaBitOp-1.0.2  
RUN make  
RUN make install  
  
RUN yum -y install git  
  
#Install Metronome  
RUN git clone https://github.com/maranda/metronome.git /usr/src/metronome  
WORKDIR /usr/src/metronome  
RUN ./configure --prefix=  
RUN make  
RUN make install  
RUN useradd -r -s /sbin/nologin -d /var/lib/metronome metronome  
RUN mkdir /var/log/metronome/  
RUN mkdir /var/run/metronome/  
RUN chown metronome:metronome /var/lib/metronome/  
RUN chown metronome:metronome /var/log/metronome/  
RUN chown metronome:metronome /var/run/metronome/  
  
#Install Metronome-modules  
ADD modules/* /lib/metronome/modules/  
  
# Add config and setup script, run it  
ADD wrappers/* /bin/  
ADD configs/metronome/metronome.cfg.lua /etc/metronome/metronome.cfg.lua  
ADD configs/metronome/ldap.cfg.lua /etc/metronome/ldap.cfg.lua  
ADD kolabgr.lua /bin/kolabgr.lua  
ADD configs/metronome/groups.txt /etc/metronome/groups.txt  
ADD configs/supervisord.conf /etc/supervisord.conf  
ADD configs/fail2ban/jail.conf /etc/fail2ban/jail.conf  
ADD configs/fail2ban/filter.d/* /etc/fail2ban/filter.d/  
ADD start.sh /bin/start.sh  
ENTRYPOINT ["/bin/start.sh"]  
  
WORKDIR /root  
  
VOLUME ["/data"]  
  
# 5000/tcp: mod_proxy65  
# 5222/tcp: client to server  
# 5269/tcp: server to server  
# 5280/tcp: BOSH  
# 5281/tcp: Secure BOSH  
EXPOSE 5000 5222 5269 5280 5281  

