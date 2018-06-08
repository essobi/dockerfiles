FROM centos:7  
  
MAINTAINER Alvaro Vega <alvaro.vegagarcia@telefonica.com>  
  
ENV ORCHESTRATOR_USER orchestrator  
  
ENV ORCHESTRATOR_VERSION 2.1.0  
  
ENV KEYSTONE_HOST localhost  
ENV KEYSTONE_PORT 5001  
ENV KEYSTONE_PROTOCOL http  
  
ENV KEYPASS_HOST localhost  
ENV KEYPASS_PORT 17070  
ENV KEYPASS_PROTOCOL http  
  
ENV ORION_HOST localhost  
ENV ORION_PORT 1026  
ENV ORION_PROTOCOL http  
  
ENV PEP_PERSEO_HOST localhost  
ENV PEP_PERSEO_PORT 1026  
ENV PEP_PERSEO_PROTOCOL http  
  
ENV STH_HOST localhost  
ENV STH_PORT 18666  
ENV STH_PROTOCOL http  
ENV STH_NOTIFYPATH notify  
  
ENV PERSEO_HOST localhost  
ENV PERSEO_PORT 19090  
ENV PERSEO_PROTOCOL http  
ENV PERSEO_NOTIFYPATH notices  
  
ENV CYGNUS_HOST localhost  
ENV CYGNUS_PORT 5050  
ENV CYGNUS_PROTOCOL http  
ENV CYGNUS_NOTIFYPATH notify  
  
ENV LDAP_HOST localhost  
ENV LDAP_PORT 389  
ENV LDAP_BASEDN dc=openstack,dc=org  
  
ENV MAILER_HOST localhost  
ENV MAILER_PORT 589  
ENV MAILER_USER smtpuser  
ENV MAILER_PASSWORD smtpuserpassword  
ENV MAILER_FROM smtpfrom  
ENV MAILER_TO smtpto  
  
ENV MONGODB_URI localhost:27017  
  
ENV python_lib /var/env-orchestrator/lib/python2.7/site-packages  
  
COPY . /opt/sworchestrator/  
  
# OLD  
# COPY ./src/ ./requirements.txt $python_lib/iotp-orchestrator/  
# COPY ./bin/* $python_lib/iotp-orchestrator/bin/  
  
WORKDIR $python_lib/iotp-orchestrator  
  
RUN \  
adduser --comment "${ORCHESTRATOR_USER}" ${ORCHESTRATOR_USER} && \  
# Install dependencies  
yum install -y epel-release && yum update -y epel-release && \  
yum install -y yum-plugin-remove-with-leaves python python-pip python-devel
openldap-devel python-virtualenv gcc ssh && \  
yum install -y tcping findutils sed && \  
mkdir -p $python_lib/iotp-orchestrator && \  
mkdir -p $python_lib/iotp-orchestrator/bin && \  
cp -rp /opt/sworchestrator/src/* $python_lib/iotp-orchestrator && cp -p
/opt/sworchestrator/requirements.txt $python_lib/iotp-orchestrator && \  
cp -rp /opt/sworchestrator/bin $python_lib/iotp-orchestrator && \  
chmod 755 $python_lib/iotp-orchestrator/bin/orchestrator-entrypoint.sh && \  
pip install -r $python_lib/iotp-orchestrator/requirements.txt && \  
pip install repoze.lru && \  
find $python_lib/iotp-orchestrator -name "*.pyc" -delete && \  
cp $python_lib/iotp-orchestrator/bin/orchestrator-daemon.sh
/etc/init.d/orchestrator && \  
cp $python_lib/iotp-orchestrator/bin/orchestrator-daemon
/etc/default/orchestrator-daemon && \  
ln -s $python_lib/iotp-orchestrator /opt/orchestrator && \  
ln -s /opt/orchestrator/orchestrator/commands /opt/orchestrator/bin/ && \  
mkdir -p /var/log/orchestrator && \  
  
# Set IOTP EndPoints in orchestrator config  
sed -i ':a;N;$!ba;s/KEYSTONE = {[A-Za-z0-9,\"\n: ]*}/KEYSTONE = { \  
\"host\": \"'$KEYSTONE_HOST'\", \  
\"port\": \"'$KEYSTONE_PORT'\", \  
\"protocol\": \"'$KEYSTONE_PROTOCOL'\" \  
}/g' /opt/orchestrator/settings/dev.py && \  
  
sed -i ':a;N;$!ba;s/KEYPASS = {[A-Za-z0-9,\"\n: ]*}/KEYPASS = { \  
\"host\": \"'$KEYPASS_HOST'\", \  
\"port\": \"'$KEYPASS_PORT'\", \  
\"protocol\": \"'$KEYPASS_PROTOCOL'\" \  
}/g' /opt/orchestrator/settings/dev.py && \  
  
sed -i ':a;N;$!ba;s/ORION = {[A-Za-z0-9,\"\n: ]*}/ORION = { \  
\"host\": \"'$ORION_HOST'\", \  
\"port\": \"'$ORION_PORT'\", \  
\"protocol\": \"'$ORION_PROTOCOL'\" \  
}/g' /opt/orchestrator/settings/dev.py && \  
  
sed -i ':a;N;$!ba;s/PEP_PERSEO = {[A-Za-z0-9,\"\n: ]*}/PEP_PERSEO = { \  
\"host\": \"'$PEP_PERSEO_HOST'\", \  
\"port\": \"'$PEP_PERSEO_PORT'\", \  
\"protocol\": \"'$PEP_PERSEO_PROTOCOL'\" \  
}/g' /opt/orchestrator/settings/dev.py && \  
  
sed -i ':a;N;$!ba;s/STH = {[A-Za-z0-9,\/\"\n: ]*}/STH = { \  
\"host\": \"'$STH_HOST'\", \  
\"port\": \"'$STH_PORT'\", \  
\"protocol\": \"'$STH_PROTOCOL'\", \  
\"notifypath\": \"\/'$STH_NOTIFYPATH'\" \  
}/g' /opt/orchestrator/settings/dev.py && \  
  
sed -i ':a;N;$!ba;s/PERSEO = {[A-Za-z0-9,\/\"\n: ]*}/PERSEO = { \  
\"host\": \"'$PERSEO_HOST'\", \  
\"port\": \"'$PERSEO_PORT'\", \  
\"protocol\": \"'$PERSEO_PROTOCOL'\", \  
\"notifypath\": \"\/'$PERSEO_NOTIFYPATH'\" \  
}/g' /opt/orchestrator/settings/dev.py && \  
  
sed -i ':a;N;$!ba;s/CYGNUS = {[A-Za-z0-9,\/\"\n: ]*}/CYGNUS = { \  
\"host\": \"'$CYGNUS_HOST'\", \  
\"port\": \"'$CYGNUS_PORT'\", \  
\"protocol\": \"'$CYGNUS_PROTOCOL'\", \  
\"notifypath\": \"\/'$CYGNUS_NOTIFYPATH'\" \  
}/g' /opt/orchestrator/settings/dev.py && \  
  
sed -i ':a;N;$!ba;s/LDAP = {[A-Za-z0-9,=@.\-\/\"\n: ]*}/LDAP = { \  
\"host\": \"'$LDAP_HOST'\", \  
\"port\": \"'$LDAP_PORT'\", \  
\"basedn\": \"'$LDAP_BASEDN'\" \  
}/g' /opt/orchestrator/settings/dev.py && \  
  
sed -i ':a;N;$!ba;s/MAILER = {[A-Za-z0-9,=@.\-\/\"\n: ]*}/MAILER = { \  
\"host\": \"'$MAILER_HOST'\", \  
\"port\": \"'$MAILER_PORT'\", \  
\"user\": \"'$MAILER_USER'\", \  
\"password\": \"'$MAILER_PASSWORD'\", \  
\"from\": \"'$MAILER_FROM'\", \  
\"to\": \"'$MAILER_TO'\" \  
}/g' /opt/orchestrator/settings/dev.py && \  
  
sed -i ':a;N;$!ba;s/MONGODB = {[A-Za-z0-9,\/\"\n: ]*}/MONGODB = { \  
\"URI\": \"mongodb:\/\/'$MONGODB_URI'\" \  
}/g' /opt/orchestrator/settings/dev.py && \  
  
# Put IOT endpoints conf into ochestrator-entrypoint.sh  
sed -i 's/KEYSTONE_PORT=5001/KEYSTONE_PORT='$KEYSTONE_PORT'/g'
/opt/orchestrator/bin/orchestrator-entrypoint.sh && \  
sed -i 's/KEYSTONE_PROTOCOL=http/KEYSTONE_PROTOCOL='$KEYSTONE_PROTOCOL'/g'
/opt/orchestrator/bin/orchestrator-entrypoint.sh && \  
sed -i 's/KEYPASS_PORT=17070/KEYPASS_PORT='$KEYPASS_PORT'/g'
/opt/orchestrator/bin/orchestrator-entrypoint.sh && \  
sed -i 's/KEYPASS_PROTOCOL=http/KEYPASS_PROTOCOL='$KEYPASS_PROTOCOL'/g'
/opt/orchestrator/bin/orchestrator-entrypoint.sh && \  
sed -i 's/ORION_PORT=1026/ORION_PORT='$ORION_PORT'/g'
/opt/orchestrator/bin/orchestrator-entrypoint.sh && \  
sed -i 's/ORION_PROTOCOL=http/ORION_PROTOCOL='$ORION_PROTOCOL'/g'
/opt/orchestrator/bin/orchestrator-entrypoint.sh && \  
sed -i 's/IOTA_PORT=4052/IOTA_PORT='$IOTA_PORT'/g'
/opt/orchestrator/bin/orchestrator-entrypoint.sh && \  
sed -i 's/IOTA_PROTOCOL=http/IOTA_PROTOCOL='$IOTA_PROTOCOL'/g'
/opt/orchestrator/bin/orchestrator-entrypoint.sh && \  
sed -i 's/PEP_PERSEO_PORT=1026/PEP_PERSEO_PORT='$PEP_PERSEO_PORT'/g'
/opt/orchestrator/bin/orchestrator-entrypoint.sh && \  
sed -i
's/PEP_PERSEO_PROTOCOL=http/PEP_PERSEO_PROTOCOL='$PEP_PERSEO_PROTOCOL'/g'
/opt/orchestrator/bin/orchestrator-entrypoint.sh && \  
sed -i 's/STH_PORT=18666/STH_PORT='$STH_PORT'/g'
/opt/orchestrator/bin/orchestrator-entrypoint.sh && \  
sed -i 's/STH_PROTOCOL=http/STH_PROTOCOL='$STH_PROTOCOL'/g'
/opt/orchestrator/bin/orchestrator-entrypoint.sh && \  
sed -i 's/PERSEO_PORT=19090/PERSEO_PORT='$PERSEO_PORT'/g'
/opt/orchestrator/bin/orchestrator-entrypoint.sh && \  
sed -i 's/PERSEO_PROTOCOL=http/PERSEO_PROTOCOL='$PERSEO_PROTOCOL'/g'
/opt/orchestrator/bin/orchestrator-entrypoint.sh && \  
sed -i 's/CYGNUS_PORT=5050/CYGNUS_PORT='$CYGNUS_PORT'/g'
/opt/orchestrator/bin/orchestrator-entrypoint.sh && \  
sed -i 's/CYGNUS_PROTOCOL=http/CYGNUS_PROTOCOL='$CYGNUS_PROTOCOL'/g'
/opt/orchestrator/bin/orchestrator-entrypoint.sh && \  
sed -i 's/CYGNUS_NOTIFYPATH=notify/CYGNUS_NOTIFYPATH='$CYGNUS_NOTIFYPATH'/g'
/opt/orchestrator/bin/orchestrator-entrypoint.sh && \  
sed -i 's/LDAP_HOST=localhost/LDAP_HOST='$LDAP_HOST'/g'
/opt/orchestrator/bin/orchestrator-entrypoint.sh && \  
sed -i 's/LDAP_PORT=389/LDAP_PORT='$LDAP_PORT'/g'
/opt/orchestrator/bin/orchestrator-entrypoint.sh && \  
sed -i 's/LDAP_BASEDN=dc=openstack,dc=org/LDAP_BASEDN='$LDAP_BASEDN'/g'
/opt/orchestrator/bin/orchestrator-entrypoint.sh && \  
sed -i 's/MAILER_HOST=localhost/MAILER_HOST='$MAILER_HOST'/g'
/opt/orchestrator/bin/orchestrator-entrypoint.sh && \  
sed -i 's/MAILER_PORT=587/MAILER_PORT='$MAILER_PORT'/g'
/opt/orchestrator/bin/orchestrator-entrypoint.sh && \  
sed -i 's/MAILER_USER=smtpuser@yourdomain.com/MAILER_USER='$MAILER_USER'/g'
/opt/orchestrator/bin/orchestrator-entrypoint.sh && \  
sed -i 's/MAILER_PASSWORD=yourpassword/MAILER_PASSWORD='$MAILER_PASSWORD'/g'
/opt/orchestrator/bin/orchestrator-entrypoint.sh && \  
sed -i 's/MAILER_FROM=smtpuser/MAILER_FROM='$MAILER_FROM'/g'
/opt/orchestrator/bin/orchestrator-entrypoint.sh && \  
sed -i 's/MAILER_TO=smtpuser/MAILER_TO='$MAILER_TO'/g'
/opt/orchestrator/bin/orchestrator-entrypoint.sh && \  
sed -i 's/MONGODB_URI=localhost:27017/MONGODB_URI='$MONGODB_URI'/g'
/opt/orchestrator/bin/orchestrator-entrypoint.sh && \  
# Put orchestrator version  
sed -i 's/ORC_version/'$ORCHESTRATOR_VERSION'/g'
/opt/orchestrator/settings/common.py && \  
sed -i 's/\${project.version}/'$ORCHESTRATOR_VERSION'/g'
/opt/orchestrator/orchestrator/core/banner.txt && \  
  
echo "INFO: Cleaning unused software..." && \  
rm -rf /opt/sworchestrator && \  
yum erase -y --remove-leaves yum-plugin-remove-with-leaves gcc && \  
# Delete pip cache  
rm -rf ~/.cache && \  
# Erase without dependencies of the document formatting system (man). This
cannot be removed using yum  
# as yum uses hard dependencies and doing so will uninstall essential packages  
rpm -qa groff redhat-logos | xargs -r rpm -e --nodeps && \  
# Clean yum data  
yum clean all && rm -rf /var/lib/yum/yumdb && rm -rf /var/lib/yum/history && \  
# Rebuild rpm data files  
rpm -vv --rebuilddb && \  
# Delete unused locales. Only preserve en_US and the locale aliases  
find /usr/share/locale -mindepth 1 -maxdepth 1 ! -name 'en_US' ! -name
'locale.alias' | xargs -r rm -r && \  
bash -c 'localedef --list-archive | grep -v -e "en_US" | xargs localedef
--delete-from-archive' && \  
# We use cp instead of mv as to refresh locale changes for ssh connections  
# We use /bin/cp instead of cp to avoid any alias substitution, which in some
cases has been problematic  
/bin/cp -f /usr/lib/locale/locale-archive /usr/lib/locale/locale-archive.tmpl
&& \  
build-locale-archive && \  
# We don't need to manage Linux account passwords requisites: lenght,
mays/mins, etc  
# This cannot be removed using yum as yum uses hard dependencies and doing so
will uninstall essential packages  
rm -rf /usr/share/cracklib && \  
# We don't need glibc locale data  
# This cannot be removed using yum as yum uses hard dependencies and doing so
will uninstall essential packages  
rm -rf /usr/share/i18n /usr/{lib,lib64}/gconv && \  
# We don't need wallpapers  
rm -rf /usr/share/wallpapers/* && \  
# Don't need old log files inside docker images  
rm -f /tmp/* /var/log/*log  
  
# Define the entry point  
ENTRYPOINT ["/opt/orchestrator/bin/orchestrator-entrypoint.sh"]  
  
EXPOSE 8084  
  

