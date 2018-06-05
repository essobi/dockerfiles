FROM clouder/clouder-base  
MAINTAINER Yannick Buron yburon@goclouder.net  
  
RUN touch /tmp/odoo-exec  
# generate locales  
RUN locale-gen en_US.UTF-8 && update-locale  
RUN echo 'LANG="en_US.UTF-8"' > /etc/default/locale  
  
# Add the PostgreSQL PGP key to verify their Debian packages.  
# It should be the same key as
https://www.postgresql.org/media/keys/ACCC4CF8.asc  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8  
  
# Add PostgreSQL's repository. It contains the most recent stable release  
# of PostgreSQL, 9.4.  
# install dependencies as distrib packages when system bindings are required  
# some of them extend the basic odoo requirements for a better "apps"
compatibility  
# most dependencies are distributed as wheel packages at the next step  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >
/etc/apt/sources.list.d/pgdg.list && apt-get update && apt-get -yq install
adduser ghostscript postgresql-client-9.4 python python-pip libjpeg-dev
libfreetype6-dev zlib1g-dev libpng12-dev python-imaging python-pychart python-
libxslt1 xfonts-base xfonts-75dpi libxrender1 libxext6 fontconfig python-zsi
python-lasso libzmq5 libxslt1-dev libxml2-dev libxml2 libxslt1.1 python-dev
libpq-dev libffi-dev libldap2-dev libssl-dev libsasl2-dev openssh-client node-
less  
  
RUN pip install --upgrade setuptools  
RUN pip install --upgrade pip  
ADD sources/requirements.txt /opt/sources/requirements.txt  
# use wheels from our public wheelhouse for proper versions of listed packages  
# as described in sourced pip-req.txt  
# these are python dependencies for odoo and "apps" as precompiled wheel
packages  
RUN pip install --upgrade --force-reinstall -r /opt/sources/requirements.txt  
  
RUN pip install paramiko erppeek  
  
# must unzip this package to make it visible as an odoo external dependency  
RUN easy_install -UZ py3o.template==0.9.5  
  
# install wkhtmltopdf based on QT5  
ADD
http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-
trusty-amd64.deb /opt/sources/wkhtmltox.deb  
RUN dpkg -i /opt/sources/wkhtmltox.deb  
  
ADD sources/bin /app/bin/  
# create the odoo user  
RUN adduser --home=/opt/odoo --disabled-password --gecos "" \--shell=/bin/bash
odoo  
RUN mkdir -p /opt/odoo/data  
RUN mkdir -p /opt/odoo/etc  
RUN mkdir -p /opt/odoo/extra-addons  
RUN mkdir -p /opt/odoo/var  
RUN chown -R odoo /opt/odoo/*  
#RUN chown -R odoo /opt/odoo/etc  
#RUN chown -R odoo /opt/odoo/extra-addons  
#RUN chown -R odoo /opt/odoo/data  
# Execution environment  
USER odoo  
CMD /opt/odoo/files/odoo/openerp-server -c /opt/odoo/etc/odoo.conf  

