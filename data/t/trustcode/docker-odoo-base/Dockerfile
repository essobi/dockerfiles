FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM=xterm  
# Avoid ERROR: invoke-rc.d: policy-rc.d denied execution of start.  
RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d  
  
##### Dependências #####  
ADD conf/apt-requirements /opt/sources/  
ADD conf/pip-requirements /opt/sources/  
  
WORKDIR /opt/sources/  
RUN apt-get update && apt-get install -y --no-install-recommends $(grep -v
'^#' apt-requirements)  
  
ADD
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.1/wkhtmltox-0.12.1_linux-
trusty-amd64.deb /opt/sources/wkhtmltox.deb  
RUN dpkg -i wkhtmltox.deb && rm wkhtmltox.deb && \  
locale-gen en_US en_US.UTF-8 pt_BR pt_BR.UTF-8 && \  
dpkg-reconfigure locales  
  
ENV LC_ALL pt_BR.UTF-8  
RUN pip3 install setuptools  
RUN pip3 install --no-cache-dir --upgrade pip  
RUN npm install -g less && npm cache clean  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN apt-get install -y gcc  
RUN pip3 install --no-cache-dir -r pip-requirements  
ADD conf/brasil-requirements /opt/sources/  
RUN pip3 install --no-cache-dir -r brasil-requirements  
  
##### Repositórios TrustCode e OCB #####  
WORKDIR /opt/odoo/  
RUN mkdir private  
  
##### Configurações Odoo #####  
ADD conf/supervisord.conf /etc/supervisor/supervisord.conf  
  
RUN mkdir /var/log/odoo && \  
mkdir /opt/dados && \  
mkdir /var/log/supervisord && \  
touch /var/log/odoo/odoo.log && \  
touch /var/run/odoo.pid && \  
ln -s /opt/odoo/odoo/odoo-bin /usr/bin/odoo-server && \  
ln -s /etc/odoo/odoo.conf && \  
ln -s /var/log/odoo/odoo.log && \  
useradd --system --home /opt --shell /bin/bash --uid 1040 odoo && \  
chown -R odoo:odoo /opt && \  
chown -R odoo:odoo /var/log/odoo && \  
chown odoo:odoo /var/run/odoo.pid  
  
##### Limpeza da Instalação #####  
RUN apt-get autoremove -y && \  
apt-get autoclean  
  
##### Finalização do Container #####  
WORKDIR /opt/odoo  

