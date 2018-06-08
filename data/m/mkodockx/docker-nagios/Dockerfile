FROM cpuguy83/ubuntu  
MAINTAINER https://m-ko-x.de Markus Kosmal <code@m-ko-x.de>  
  
# stick to nagios 3.5.1 as newer ones are not usable  
# setting defaults  
ENV NAGIOS_HOME /opt/nagios  
ENV NAGIOS_USER nagios  
ENV NAGIOS_GROUP nagios  
ENV NAGIOS_CMDUSER nagios  
ENV NAGIOS_CMDGROUP nagios  
ENV NAGIOSADMIN_USER nagiosadmin  
ENV NAGIOSADMIN_PASS nagios  
ENV APACHE_RUN_USER nagios  
ENV APACHE_RUN_GROUP nagios  
ENV NAGIOS_TIMEZONE UTC  
  
# install prerequesites  
RUN sed -i 's/universe/universe multiverse/' /etc/apt/sources.list && \  
apt-get update && apt-get install -y unzip libssl-dev iputils-ping netcat
build-essential snmp snmpd snmp-mibs-downloader php5-cli apache2
libapache2-mod-php5 runit bc postfix bsd-mailx && \  
( egrep -i "^${NAGIOS_GROUP}" /etc/group || groupadd $NAGIOS_GROUP ) && (
egrep -i "^${NAGIOS_CMDGROUP}" /etc/group || groupadd $NAGIOS_CMDGROUP ) && \  
( id -u $NAGIOS_USER || useradd --system $NAGIOS_USER -g $NAGIOS_GROUP -d
$NAGIOS_HOME ) && ( id -u $NAGIOS_CMDUSER || useradd --system -d $NAGIOS_HOME
-g $NAGIOS_CMDGROUP $NAGIOS_CMDUSER ) && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
ADD ./nagios /tmp/nagios  
ADD ./nagios-plugins-1.5 /tmp/nagios-plugins-1.5  
  
RUN cd /tmp/nagios && ./configure --prefix=${NAGIOS_HOME} \--exec-
prefix=${NAGIOS_HOME} \--enable-event-broker --with-nagios-command-
user=${NAGIOS_CMDUSER} \--with-command-group=${NAGIOS_CMDGROUP} \--with-
nagios-user=${NAGIOS_USER} \--with-nagios-group=${NAGIOS_GROUP} \--with-
openssl=/usr/bin/openssl && make all && make install && make install-config &&
make install-commandmode && cp sample-config/httpd.conf
/etc/apache2/conf.d/nagios.conf && \  
cd /tmp/nagios-plugins-1.5 && ./configure --prefix=${NAGIOS_HOME} && make &&
make install && \  
sed -i.bak 's/.*\=www\\-data//g' /etc/apache2/envvars  
  
# export global conf fata  
RUN export DOC_ROOT="DocumentRoot $(echo $NAGIOS_HOME/share)"; sed -i
"s,DocumentRoot.*,$DOC_ROOT," /etc/apache2/sites-enabled/000-default  
  
# create and configure nagios data  
RUN ln -s ${NAGIOS_HOME}/bin/nagios /usr/local/bin/nagios && mkdir -p
/usr/share/snmp/mibs && chmod 0755 /usr/share/snmp/mibs && touch
/usr/share/snmp/mibs/.foo  
  
# set nagios timezone  
RUN echo "use_timezone=$NAGIOS_TIMEZONE" >> ${NAGIOS_HOME}/etc/nagios.cfg &&
echo "SetEnv TZ \"${NAGIOS_TIMEZONE}\"" >> /etc/apache2/conf.d/nagios.conf  
  
# config startup configs  
RUN mkdir -p ${NAGIOS_HOME}/etc/conf.d && mkdir -p ${NAGIOS_HOME}/etc/monitor
&& ln -s /usr/share/snmp/mibs ${NAGIOS_HOME}/libexec/mibs  
  
# modify setup to find configs  
RUN echo "cfg_dir=${NAGIOS_HOME}/etc/conf.d" >> ${NAGIOS_HOME}/etc/nagios.cfg
&& \  
echo "cfg_dir=${NAGIOS_HOME}/etc/monitor" >> ${NAGIOS_HOME}/etc/nagios.cfg  
  
# setup mail  
RUN download-mibs && echo "mibs +ALL" > /etc/snmp/snmp.conf && \  
sed -i 's,/bin/mail,/usr/bin/mail,' /opt/nagios/etc/objects/commands.cfg && \  
sed -i 's,/usr/usr,/usr,' /opt/nagios/etc/objects/commands.cfg  
  
# copy service data/binaries  
RUN cp /etc/services /var/spool/postfix/etc/ && \  
mkdir -p /etc/sv/nagios && mkdir -p /etc/sv/apache && rm -rf /etc/sv/getty-5
&& mkdir -p /etc/sv/postfix  
  
# add runnables  
ADD nagios.init /etc/sv/nagios/run  
ADD apache.init /etc/sv/apache/run  
ADD postfix.init /etc/sv/postfix/run  
ADD postfix.stop /etc/sv/postfix/finish  
  
# add bootstrap script  
ADD start.sh /usr/local/bin/start_nagios  
  
# get theme  
RUN mkdir -p /tmp/theme && cd /tmp/theme && wget -o theme.zip
http://sourceforge.net/projects/arana-nagios/files/arana_style-1.0for-
Nagios3x-ENG.zip && \  
unzip theme.zip -d ${NAGIOS_HOME}/share/  
  
ENV APACHE_LOCK_DIR /var/run  
ENV APACHE_LOG_DIR /var/log/apache2  
  
EXPOSE 80  
VOLUME ["/opt/nagios/var", "/opt/nagios/etc", "/opt/nagios/libexec",
"/var/log/apache2", "/usr/share/snmp/mibs"]  
  
CMD ["/usr/local/bin/start_nagios"]  

