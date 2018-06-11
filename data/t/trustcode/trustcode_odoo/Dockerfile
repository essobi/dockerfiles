FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM=xterm  
# Avoid ERROR: invoke-rc.d: policy-rc.d denied execution of start.  
RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d  
  
##### Dependências #####  
ADD conf/apt-requirements /opt/sources/  
ADD conf/pip-requirements /opt/sources/  
ADD http://download.gna.org/wkhtmltopdf/0.12/0.12.1/wkhtmltox-0.12.1_linux-
trusty-amd64.deb /opt/sources/wkhtmltox.deb  
  
WORKDIR /opt/sources/  
RUN apt-get update && apt-get install -y nano python-dev python-pip locales  
RUN pip install --upgrade pip  
RUN apt-get install -y --no-install-recommends $(grep -v '^#' apt-
requirements)  
  
RUN pip install -r pip-requirements && \  
dpkg -i wkhtmltox.deb && \  
locale-gen en_US en_US.UTF-8 pt_BR.UTF-8 && \  
dpkg-reconfigure locales  
  
##### Instala e Configura o POSTGRESQL #####  
ADD https://www.postgresql.org/media/keys/ACCC4CF8.asc ./chave.asc  
RUN apt-key add chave.asc  
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main' 9.4 >
/etc/apt/sources.list.d/pgdg.list  
  
RUN apt-get update && apt-get install -y postgresql  
  
USER postgres  
RUN /etc/init.d/postgresql start && psql -c "CREATE USER odoo WITH CREATEDB
SUPERUSER PASSWORD 'odoo';"  
  
USER root  
RUN mkdir -p /run/postgres && \  
chown -R postgres /var/lib/postgresql/ && \  
chmod g+s /run/postgresql && \  
chmod g+s /run/postgresql && \  
chown -R postgres:postgres /run/postgresql  
  
##### Repositórios TrustCode e OCB #####  
RUN apt-get update && apt-get install -y supervisor git  
WORKDIR /opt/odoo/  
RUN git clone -b 8.0 http://github.com/OCA/OCB.git OCB  
RUN git clone -b 8.0 http://github.com/Trust-Code/odoo-brazil-eletronic-
documents.git eletronic-docs  
RUN git clone -b 8.0 http://github.com/Trust-Code/l10n-brazil.git l10n-brazil  
RUN git clone -b 8.0 http://github.com/Trust-Code/account-fiscal-rule.git
fiscal-rule  
RUN git clone -b 8.0 http://github.com/Trust-Code/trust-addons.git trust-
addons  
RUN git clone -b 8.0 http://github.com/Trust-Code/server-tools.git server-
tools  
RUN git clone -b 8.0 https://github.com/Trust-Code/account-payment.git  
RUN git clone -b 8.0 http://github.com/OCA/bank-payment.git  
RUN git clone -b 8.0 http://github.com/OCA/sale-workflow.git  
RUN git clone -b 8.0 https://github.com/Trust-Code/account-invoicing.git  
RUN git clone -b 8.0 https://github.com/OCA/bank-statement-import.git  
RUN git clone -b 8.0 https://github.com/Trust-Code/odoo-brazil-banking.git  
  
RUN git clone https://github.com/Trust-Code/PySPED.git pysped  
RUN mkdir private  
  
##### Configurações Odoo #####  
ADD conf/odoo.conf /etc/odoo/  
ADD conf/supervisord.conf /etc/supervisor/supervisord.conf  
  
RUN mkdir /var/log/odoo && \  
mkdir /opt/dados && \  
mkdir /opt/xml && \  
mkdir /opt/xml/imp && \  
mkdir /opt/xml/exp && \  
mkdir /opt/xml/bkp && \  
touch /var/log/odoo/odoo.log && \  
touch /var/run/odoo.pid && \  
ln -s /opt/odoo/OCB/openerp-server /usr/bin/odoo-server && \  
useradd --system --home /opt --shell /bin/bash odoo && \  
chown -R odoo:odoo /opt && \  
chown -R odoo:odoo /etc/odoo/odoo.conf && \  
chown -R odoo:odoo /var/log/odoo && \  
chown odoo:odoo /var/run/odoo.pid  
  
##### Instalação do PySPED #####  
RUN mkdir /tmp/.python-eggs && chown -R odoo /tmp/.python-eggs  
ENV PYTHON_EGG_CACHE /tmp/.python-eggs  
WORKDIR /opt/odoo/pysped  
RUN python setup.py install  
  
##### Limpeza da Instalação #####  
RUN apt-get autoremove -y && \  
apt-get autoclean  
  
##### Finalização do Container #####  
EXPOSE 5432  
WORKDIR /opt/odoo  
  
VOLUME ["/opt/", "/etc/odoo"]  
CMD ["/usr/bin/supervisord"]  

