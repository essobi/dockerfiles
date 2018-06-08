FROM yajo/centos-epel  
  
MAINTAINER yajo@openaliasbox.org  
  
# Launcher will patch configuration on first run and launch Odoo  
CMD launch  
  
# Odoo ports for web and chat  
EXPOSE 8069 8072  
# Variables used by the launch scripts  
ENV ADMIN_PASSWORD=admin \  
ODOO_SERVER=odoo.py \  
UNACCENT=True \  
PGUSER=odoo \  
PGPASSWORD=odoo \  
PGHOST=db \  
PGDATABASE=odoo \  
# Variables used by the WDB debugger, in case you link a WDB container  
WDB_NO_BROWSER_AUTO_OPEN=True \  
WDB_SOCKET_SERVER=wdb \  
WDB_WEB_PORT=1984 \  
WDB_WEB_SERVER=localhost  
  
# Install Odoo and psql (to install unaccent automatically)  
RUN yum -y install postgresql
http://nightly.odoo.com/10.0/nightly/rpm/odoo_10.0.latest.noarch.rpm && \  
  
# Extra dependencies. TODO remove them when not needed. See:  
# - https://github.com/odoo/odoo/issues/4021  
# - https://github.com/odoo/odoo/issues/9186  
# - https://github.com/odoo/odoo/issues/10067  
# - https://github.com/odoo/odoo/issues/10947  
# - http://stackoverflow.com/a/31926346/1468388  
yum -y install \  
mailcap poppler-utils python-gevent python-inotify python-pip file \  
gettext && \  
  
# Need babel >= 1.0, CentOS' version is older  
pip install --upgrade babel && \  
  
# Cannot use CentOS version of wkhtmltopdf because it's not patched to work  
# without an X server, so let's install the official upstream RPM instead  
yum -y install
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.2.1/wkhtmltox-0.12.2.1_linux-
centos7-amd64.rpm && \  
# Add openupgradelib for your migrations  
pip install openupgradelib && \  
# Add a debugger and additional dependencies  
yum -y install gcc python-devel freetype fontconfig bzip2 npm \  
ruby-devel rubygems && \  
pip install wdb && \  
npm install --global phantomjs && \  
gem install sass bootstrap-sass compass && \  
# Add locales  
yum -y reinstall glibc-common && \  
  
yum -y remove '*-devel' && yum clean all && \  
# Create path for extra addons  
mkdir --parents /opt/odoo/extra-addons && \  
# Create odoo $HOME to store some data  
mkdir /home/odoo && \  
chown odoo:odoo /home/odoo && \  
# Configure launchers  
touch /firstrun  
ADD 00-base.conf.tpl /etc/odoo/  
ADD debug launch pot unittest /usr/local/bin/  
RUN chmod a+rx /usr/local/bin/*  
  
# Folders modified at runtime by Odoo  
VOLUME ["/home/odoo", "/var/lib/odoo", "/var/log/odoo"]  

