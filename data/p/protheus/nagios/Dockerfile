# Nagios Distrib  
FROM protheus/centos-nagios:latest  
MAINTAINER Protheus <sauvage.jeff@gmail.com>  
  
ENV NAGIOS_HOME /opt/nagios  
ENV NAGIOS_GRAPH /opt/nagiosgraph  
ENV NAGIOS_USER nagios  
ENV NAGIOS_GROUP nagios  
ENV NAGIOS_CMDUSER nagios  
ENV NAGIOS_CMDGROUP nagios  
ENV NAGIOSADMIN_USER nagiosadmin  
ENV NAGIOSADMIN_PASS nagiosadmin  
ENV APACHE_RUN_USER nagios  
ENV APACHE_RUN_GROUP nagios  
ENV NAGIOS_TIMEZONE UTC  
ENV NAGIOS_CONFIG_FILE ${NAGIOS_HOME}/etc/nagios.cfg  
ENV NAGIOS_CGI_DIR ${NAGIOS_HOME}/sbin  
ENV NG_WWW_DIR ${NAGIOS_HOME}/share/nagiosgraph  
ENV NG_CGI_URL /nagiosgraph/cgi-bin  
  
  
# make temporary Installation directory  
RUN mkdir /tmp/install  
  
# Create Users and Groups  
RUN ( egrep -i "^${NAGIOS_GROUP}" /etc/group || groupadd $NAGIOS_GROUP ) && \  
( egrep -i "^${NAGIOS_CMDGROUP}" /etc/group || groupadd $NAGIOS_CMDGROUP )  
RUN ( id -u $NAGIOS_USER || useradd --system -d $NAGIOS_HOME -g $NAGIOS_GROUP
$NAGIOS_USER ) && \  
( id -u $NAGIOS_CMDUSER || useradd --system -d $NAGIOS_HOME -g
$NAGIOS_CMDGROUP $NAGIOS_CMDUSER )  
  
# Install Perl modules  
RUN cpanm Module::Build  
RUN cpanm Nagios::Config  
  
# install Nagios Core  
RUN cd /tmp/install && \  
git clone https://github.com/NagiosEnterprises/nagioscore.git && \  
cd nagioscore && \  
git checkout master && \  
./configure \  
\--prefix=${NAGIOS_HOME} \  
\--exec-prefix=${NAGIOS_HOME} \  
\--enable-event-broker \  
\--with-nagios-command-user=${NAGIOS_CMDUSER} \  
\--with-command-group=${NAGIOS_CMDGROUP} \  
\--with-nagios-user=${NAGIOS_USER} \  
\--with-nagios-group=${NAGIOS_GROUP} && \  
make all && \  
make install-init && \  
make install && \  
make install-config && \  
make install-commandmode && \  
make install-webconf && \  
make clean  
  
# Configure Apache  
RUN sed -i "s,User apache,User ${NAGIOS_USER}," /etc/httpd/conf/httpd.conf &&
\  
sed -i "s,Group apache,Group ${NAGIOS_GROUP}," /etc/httpd/conf/httpd.conf  
  
# Install Nagios Plugins  
RUN cd /tmp/install && \  
git clone https://github.com/nagios-plugins/nagios-plugins.git && \  
cd nagios-plugins && \  
git checkout master && \  
./tools/setup && \  
./configure \  
\--prefix=${NAGIOS_HOME} && \  
make && \  
make install && \  
make clean && \  
mkdir -p /usr/lib/nagios/plugins && \  
ln -sf ${NAGIOS_HOME}/libexec/utils.pm /usr/lib/nagios/plugins  
  
# Install Nagios NRPE  
RUN cd /tmp/install && \  
git clone https://github.com/NagiosEnterprises/nrpe.git && \  
cd nrpe && \  
git checkout master && \  
./configure \  
\--with-ssl=/usr/bin/openssl \  
\--with-ssl-lib=/usr/lib64 && \  
make check_nrpe && \  
cp src/check_nrpe ${NAGIOS_HOME}/libexec/ && \  
make clean  
  
# Install Nagios Graph  
RUN cd /tmp/install && \  
git clone git://git.code.sf.net/p/nagiosgraph/git nagiosgraph && \  
cd nagiosgraph && \  
./install.pl --install \  
\--prefix ${NAGIOS_GRAPH} \  
\--nagios-user ${NAGIOS_USER} \  
\--www-user ${NAGIOS_USER} \  
\--nagios-perfdata-file ${NAGIOS_HOME}/var/perfdata.log \  
\--nagios-cgi-url ${NG_CGI_URL} && \  
cp share/nagiosgraph.ssi ${NAGIOS_HOME}/share/ssi/common-header.ssi  
  
RUN cat ${NAGIOS_GRAPH}/etc/nagiosgraph-nagios.cfg >>
${NAGIOS_HOME}/etc/nagios.cfg && \  
cat ${NAGIOS_GRAPH}/etc/nagiosgraph-commands.cfg >>
${NAGIOS_HOME}/etc/objects/commands.cfg && \  
cp ${NAGIOS_GRAPH}/etc/nagiosgraph-apache.conf
/etc/httpd/conf.d/nagiosgraph.conf && \  
echo define service \\{ >> ${NAGIOS_HOME}/etc/objects/templates.cfg &&\  
echo name nagiosgraph >> ${NAGIOS_HOME}/etc/objects/templates.cfg &&\  
echo action_url
${NG_CGI_URL}/show.cgi?host=\$HOSTNAME\$\&service=\$SERVICEDESC\$ >>
${NAGIOS_HOME}/etc/objects/templates.cfg &&\  
echo register 0 >> ${NAGIOS_HOME}/etc/objects/templates.cfg &&\  
echo } >> ${NAGIOS_HOME}/etc/objects/templates.cfg &&\  
sed -i "s,local-service,local-service\,nagiosgraph,"
${NAGIOS_HOME}/etc/objects/localhost.cfg  
  
## Configure nagiosgraph in apache  
ADD files/www/nagiosgraph.conf /etc/httpd/conf.d/nagiosgraph.tpl  
RUN envsubst < "/etc/httpd/conf.d/nagiosgraph.tpl" >
"/etc/httpd/conf.d/nagiosgraph.conf" && rm -f
/etc/httpd/conf.d/nagiosgraph.tpl  
  
# Install other Nagios Plugins  
RUN cd /tmp/install && \  
git clone http://github.com/willixix/naglio-plugins.git WL-Nagios-Plugins && \  
git clone https://github.com/JasonRivers/nagios-plugins.git JR-Nagios-Plugins
&& \  
git clone https://github.com/justintime/nagios-plugins.git JE-Nagios-Plugins
&& \  
cp ./WL-Nagios-Plugins/*.pl ${NAGIOS_HOME}/libexec/ && \  
cp ./WL-Nagios-Plugins/*.pm ${NAGIOS_HOME}/libexec/ && \  
cp ./JR-Nagios-Plugins/check_* ${NAGIOS_HOME}/libexec/ && \  
cp ./JE-Nagios-Plugins/check_mem/check_mem.pl ${NAGIOS_HOME}/libexec/  
  
#Configure startup  
RUN mkdir /var/log/startup  
RUN /bin/rm -f /etc/rc.d/rc.local  
ADD files/rc.local /etc/rc.d/rc.local  
RUN mkdir /etc/rc.d/startup  
RUN chmod a+x /etc/rc.d/rc.local  
  
# Add nuvola FrontEnd  
RUN mkdir /tmp/install/nagios-nuvola  
ADD files/tarball/nagios-nuvola-1.0.3.tar.gz /tmp/install/nagios-
nuvola/nagios-nuvola-1.0.3.tar.gz  
RUN cd /tmp/install/nagios-nuvola && \  
gzip -d nagios-nuvola-1.0.3.tar.gz && \  
tar -zxf nagios-nuvola-1.0.3.tar && \  
/bin/cp -rf ./html/* ${NAGIOS_HOME}/share/  
  
# Add Configuration FrontEnd  
RUN cd /tmp/install && \  
git clone -b master git://lilac--reloaded.git.sourceforge.net/gitroot/lilac--
reloaded/lilac--reloaded lilac && \  
cd lilac && \  
mkdir ${NAGIOS_HOME}/share/lilac && \  
cp -r ./* ${NAGIOS_HOME}/share/lilac/ && \  
touch ${NAGIOS_HOME}/share/lilac/includes/lilac-conf.php && \  
chown -R ${NAGIOS_USER}:${NAGIOS_GROUP} ${NAGIOS_HOME}/share/* && \  
chmod a+w ${NAGIOS_HOME}/share/lilac/includes/lilac-conf.php  
  
## Configure MariaDB for lilac  
ADD files/initnagios.sh /etc/rc.d/startup/initnagios.sh  
  
# Configure sudo for lilac  
RUN sed -i "s,Defaults requiretty,#Defaults requiretty," /etc/sudoers  
RUN echo "${NAGIOS_USER} ALL=(ALL) NOPASSWD: /usr/bin/nmap *" >
/etc/sudoers.d/nagios  
RUN echo "${NAGIOS_USER} ALL=(ALL) NOPASSWD: /usr/bin/systemctl *" >>
/etc/sudoers.d/nagios  
  
# Create redirect to nagios WebUI  
ADD files/www/index.html /var/www/html/index.html  
  
# Set Passwd  
RUN htpasswd -bc ${NAGIOS_HOME}/etc/htpasswd.users ${NAGIOSADMIN_USER}
${NAGIOSADMIN_PASS}  
  
# Config Services  
RUN systemctl enable mariadb  
RUN systemctl enable httpd  
RUN systemctl enable nagios  
  
# Backup config  
RUN mkdir -p /tmp/nagios_conf  
RUN cp -r ${NAGIOS_HOME}/etc /tmp/nagios_conf  
RUN cp -r ${NAGIOS_HOME}/var /tmp/nagios_conf  
  
#Configure startup  
ADD files/initconf.sh /etc/rc.d/startup/initconf.sh  
RUN chmod a+x /etc/rc.d/startup/*  
  
#Remove install files  
RUN /bin/rm -rf /tmp/install  
  
EXPOSE 80  
VOLUME "/opt/nagios/etc" "/opt/nagios/var" "/opt/nagios/libexec"
"/var/log/httpd"  
  
ENTRYPOINT ["/usr/sbin/init"]  

