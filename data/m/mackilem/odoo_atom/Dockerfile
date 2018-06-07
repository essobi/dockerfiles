FROM trustcode/odoo-base  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOSTNAME Odoo-Atom  
  
##### Configurações Odoo #####  
RUN mkdir /var/log/odoo && \  
mkdir /opt/dados && \  
mkdir /opt/xml && \  
mkdir /opt/xml/imp && \  
mkdir /opt/xml/exp && \  
mkdir /opt/xml/bkp && \  
touch /var/log/odoo/odoo.log && \  
touch /var/run/odoo.pid && \  
ln -s /opt/odoo/OCB/openerp-server /usr/bin/odoo-server  
  
RUN useradd --system --home /opt --shell /bin/bash odoo && \  
chown -R odoo:odoo /opt && \  
chown -R odoo:odoo /var/log/odoo && \  
chown odoo:odoo /var/run/odoo.pid  
  
##### Instalação do PySPED #####  
RUN apt-get update && apt-get install -y git  
  
WORKDIR /opt/odoo  
RUN git clone \--depth=1 https://github.com/Trust-Code/PySPED.git pysped  
  
RUN mkdir /tmp/.python-eggs && chown -R odoo /tmp/.python-eggs  
ENV PYTHON_EGG_CACHE /tmp/.python-eggs  
  
WORKDIR /opt/odoo/pysped  
RUN python setup.py install  
  
WORKDIR /opt/odoo/  

