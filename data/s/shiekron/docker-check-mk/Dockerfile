# install nagios 4.0.8 / nagios plugins 2.0.3 / pnp4nagios 0.6.24 / check_mk
1.2.5i6p2 on Ubuntu  
FROM ubuntu:14.04  
# info  
MAINTAINER Joe Ortiz version: 0.3  
ENV NAGIOS_VERSION 4.0.8  
ENV NAGIOS_PLUGINS_VERSION 2.0.3  
ENV PNP4NAGIOS_VERSION 0.6.24  
ENV CHECKMK_VERSION 1.2.5i6p4  
ENV CHECKMKAGENT_VERSION 1.2.5i6p4-2_all  
  
# update container  
RUN apt-get update && \  
apt-get install -y apache2 \  
libapache2-mod-php5 \  
libapache2-mod-python \  
libgd2-xpm-dev \  
traceroute \  
sudo \  
supervisor \  
rrdtool \  
rrdcached \  
librrdtool-oo-perl \  
php5 \  
php5-gd \  
snmp \  
python-pip \  
xinetd && \  
apt-get autoclean  
  
# users and groups  
RUN adduser nagios  
RUN groupadd nagcmd  
RUN usermod -a -G nagcmd nagios  
RUN usermod -a -G nagcmd www-data  
  
ENV BUILD_PKGS build-essential bzip2 dpkg-dev fakeroot g++ g++-4.7
libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl
libdpkg-perl libfile-fcntllock-perl libidn11 libstdc++6-4.7-dev libtimedate-
perl make patch wget  
  
# install nagios  
RUN apt-get update && \  
apt-get install -y $BUILD_PKGS && \  
wget -nv -O /nagios-$NAGIOS_VERSION.tar.gz
http://downloads.sourceforge.net/project/nagios/nagios-4.x/nagios-4.0.8/nagios-$NAGIOS_VERSION.tar.gz
&& \  
tar xf nagios-$NAGIOS_VERSION.tar.gz && \  
cd nagios-$NAGIOS_VERSION && \  
./configure --with-command-group=nagcmd --with-httpd-conf=/etc/apache2/conf-
enabled && \  
make all && \  
make install && \  
make install-config && \  
make install-commandmode && \  
make install-webconf && \  
apt-get autoremove -y $BUILD_PKGS && \  
apt-get autoclean && \  
rm -fr /nagios-$NAGIOS_VERSION.tar.gz /nagios-$NAGIOS_VERSION  
  
# user/password = nagiosadmin/nagiosadmin  
RUN echo "nagiosadmin:M.t9dyxR3OZ3E" > /usr/local/nagios/etc/htpasswd.users  
RUN chown nagios:nagios /usr/local/nagios/etc/htpasswd.users  
  
# install plugins  
RUN apt-get update && \  
apt-get install -y $BUILD_PKGS && \  
wget -nv -O /nagios-plugins-$NAGIOS_PLUGINS_VERSION.tar.gz http://nagios-
plugins.org/download/nagios-plugins-$NAGIOS_PLUGINS_VERSION.tar.gz && \  
tar xf nagios-plugins-$NAGIOS_PLUGINS_VERSION.tar.gz && \  
cd nagios-plugins-$NAGIOS_PLUGINS_VERSION && \  
./configure --with-nagios-user=nagios --with-nagios-group=nagcmd && \  
make && \  
make install && \  
apt-get autoremove -y $BUILD_PKGS && \  
apt-get autoclean && \  
rm -fr /nagios-plugins-$NAGIOS_PLUGINS_VERSION.tar.gz /nagios-
plugins-$NAGIOS_PLUGINS_VERSION  
  
# install pnp4nagios  
RUN apt-get update && \  
apt-get install -y $BUILD_PKGS && \  
wget -nv -O /pnp4nagios-$PNP4NAGIOS_VERSION.tar.gz
http://downloads.sourceforge.net/project/pnp4nagios/PNP-0.6/pnp4nagios-$PNP4NAGIOS_VERSION.tar.gz
&& \  
tar xf pnp4nagios-$PNP4NAGIOS_VERSION.tar.gz && \  
cd pnp4nagios-$PNP4NAGIOS_VERSION && \  
./configure --with-nagios-user=nagios --with-nagios-group=nagcmd --with-httpd-
conf=/etc/apache2/conf-enabled --with-perfdata-dir=/data/perfdata --with-
perfdata-spool-dir=/data/perfspool && \  
make all && \  
make fullinstall && \  
apt-get autoremove -y $BUILD_PKGS && \  
apt-get autoclean && \  
rm -fr /pnp4nagios-$PNP4NAGIOS_VERSION.tar.gz /pnp4nagios-$PNP4NAGIOS_VERSION
/usr/local/pnp4nagios/share/install.php
/usr/local/pnp4nagios/etc/config_local.php  
  
COPY pnp4nagios/config.php /usr/local/pnp4nagios/etc/config.php  
COPY pnp4nagios/process_perfdata.cfg
/usr/local/pnp4nagios/etc/process_perfdata.cfg  
  
# install check_mk  
COPY check_mk/check_mk_setup.conf /root/.check_mk_setup.conf  
RUN sed -i "s/NAGIOS_VERSION/$NAGIOS_VERSION/g" /root/.check_mk_setup.conf  
RUN apt-get update && \  
apt-get install -y $BUILD_PKGS && \  
wget -nv -O /check_mk-$CHECKMK_VERSION.tar.gz http://mathias-
kettner.com/download/check_mk-$CHECKMK_VERSION.tar.gz && \  
tar xf check_mk-$CHECKMK_VERSION.tar.gz && \  
cd check_mk-$CHECKMK_VERSION && \  
./setup.sh --yes && \  
wget -nv -O /check_mk-agent_${CHECKMKAGENT_VERSION}.deb http://mathias-
kettner.com/download/check-mk-agent_${CHECKMKAGENT_VERSION}.deb && \  
dpkg -i /check_mk-agent_${CHECKMKAGENT_VERSION}.deb && \  
apt-get autoremove -y $BUILD_PKGS && \  
apt-get autoclean && \  
echo "all_hosts = [ 'localhost' ]" > /data/check_mk_conf/main.mk && \  
rm -fr /check_mk-$CHECKMK_VERSION.tar.gz /check_mk-$CHECKMK_VERSION
/root/.check_mk_setup.conf /check_mk-agent_${CHECKMKAGENT_VERSION}.deb  
  
# Extra Monitoring Modules  
# ElasticSearch Plugin to /usr/local/bin/check_elasticsearch  
RUN pip install nagios-plugin-elasticsearch  
  
# RUN touch /var/www/html/index.html  
COPY nagios/nagios.cfg /usr/local/nagios/etc/nagios.cfg  
COPY nagios/bulknpcd.cfg /usr/local/nagios/etc/objects/bulknpcd.cfg  
COPY nagios/nagios.init /etc/init.d/nagios  
RUN chmod 755 /etc/init.d/nagios  
RUN mkdir /var/run/rrdcached  
RUN chown nagios.nagcmd -R /usr/local/nagios/var/rw /data /var/run/rrdcached  
RUN chmod g+s /usr/local/nagios/var/rw  
RUN chmod -R g+w /data/mkeventd /data/check_mk_conf /data/check_mk  
  
# supervisor configuration  
COPY supervisord.conf /etc/supervisor/supervisord.conf  
  
VOLUME /data  
VOLUME /usr/local/nagios/var  
  
ADD /bin/start /bin/start  
ENTRYPOINT [ "/bin/bash" ]  
CMD [ "/bin/start" ]  
  
EXPOSE 80  

