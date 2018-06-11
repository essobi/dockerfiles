# based on https://github.com/sqawasmi/odoo-docker/blob/v8/Dockerfile  
FROM ubuntu:14.04  
MAINTAINER Ying Liu - www.MindIsSoftware.com  
  
# the GitHub branch name  
ENV ODOO_VERSION 8.0  
# the database settings should match postgresql settings  
ENV ODOO_USER odoo  
ENV ODOO_USER_PASSWORD $ODOO_USER  
ENV ODOO_DB_USER $ODOO_USER  
ENV ODOO_DB_PASSWORD $ODOO_USER  
ENV ODOO_DB_HOST odoodb  
  
# !!! EXPOSE port doesn's support ENV variable, has to change EXPOSE command  
ENV ODOO_DB_PORT 5432  
ENV ODOO_XMLRPC_PORT 8069  
# the directories and files for source code, addons, log and config  
ENV ODOO_HOME_DIR /opt/$ODOO_USER  
ENV ODOO_SERVER_DIR $ODOO_HOME_DIR/$ODOO_USER-server  
ENV ODOO_CONFIG_DIR $ODOO_HOME_DIR/etc  
ENV ODOO_CONFIG_FILE $ODOO_CONFIG_DIR/$ODOO_USER-server.conf  
ENV ODOO_LOG_DIR $ODOO_HOME_DIR/log  
ENV ODOO_LOG_FILE $ODOO_LOG_DIR/$ODOO_USER-server.log  
ENV ODOO_ADDONS_DIR $ODOO_HOME_DIR/addons  
  
ENV ODOO_SSH_PORT 2222  
# disable warning  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# install Odoo supporting packages  
RUN apt-get install -y git python-pip python-dateutil python-feedparser
python-ldap python-libxslt1 python-lxml python-mako python-openid python-
psycopg2 python-pybabel python-pychart python-pydot python-pyparsing python-
reportlab python-simplejson python-tz python-vatnumber python-vobject python-
webdav python-werkzeug python-xlwt python-yaml python-zsi python-docutils
python-psutil python-mock python-unittest2 python-jinja2 python-pypdf python-
decorator  
  
RUN pip install gdata  
  
# add user and directories  
RUN adduser --quiet --disabled-password -shell=/bin/bash --home=$ODOO_HOME_DIR
\--gecos "ODOO" $ODOO_USER  
RUN echo "$ODOO_USER:$ODOO_USER_PASSWORD" | chpasswd  
  
RUN mkdir -p $ODOO_CONFIG_DIR  
RUN mkdir -p $ODOO_LOG_DIR  
RUN mkdir -p $ODOO_ADDONS_DIR  
  
# clone source code from GitHub  
RUN git clone \--branch $ODOO_VERSION https://www.github.com/odoo/odoo
$ODOO_SERVER_DIR/  
  
# copy configuration file  
RUN cp $ODOO_SERVER_DIR/debian/openerp-server.conf $ODOO_CONFIG_FILE  
RUN chmod 640 $ODOO_CONFIG_FILE  
  
RUN chown -R $ODOO_USER:$ODOO_USER $ODOO_HOME_DIR/*  
  
# config odoo databsse  
RUN sed -i "s/db_user = .*/db_user = $ODOO_DB_USER/g" $ODOO_CONFIG_FILE  
RUN sed -i "s/db_password = .*/db_password = $ODOO_DB_PASSWORD/g"
$ODOO_CONFIG_FILE  
RUN sed -i "s/db_port = .*/db_port = $ODOO_DB_PORT/g" $ODOO_CONFIG_FILE  
RUN sed -i "s/db_host = .*/db_host = $ODOO_DB_HOST/g" $ODOO_CONFIG_FILE  
RUN echo "addons_path = $ODOO_SERVER_DIR/addons,$ODOO_ADDONS_DIR" >>
$ODOO_CONFIG_FILE  
RUN echo "logfile = /opt/odoo/log/odoo-server.log" >> $ODOO_CONFIG_FILE  
RUN echo "xmlrpc_port = $ODOO_XMLRPC_PORT" >> $ODOO_CONFIG_FILE  
  
EXPOSE 2222 8069  
ENTRYPOINT su -c "/opt/odoo/odoo-server/openerp-server
--config=/opt/odoo/etc/odoo-server.conf" -s /bin/sh odoo  

