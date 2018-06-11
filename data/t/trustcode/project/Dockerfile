FROM trustcode/odoo-base  
  
MAINTAINER Mackilem Van der Laan <comercial@trustcode.com.br> Danimar Ribeiro
<desenvolvimento@trustcode.com.br>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
##### Repositórios TrustCode e OCB #####  
RUN apt-get update && apt-get install -y supervisor git  
WORKDIR /opt/odoo/  
RUN git clone -b 8.0 --depth=1 http://github.com/OCA/OCB.git OCB  
RUN git clone -b 8.0 --depth=1 http://github.com/Trust-Code/odoo-brazil-
eletronic-documents.git eletronic-docs  
RUN git clone -b 8.0 --depth=1 http://github.com/Trust-Code/l10n-brazil.git
l10n-brazil  
RUN git clone -b 8.0 --depth=1 http://github.com/Trust-Code/account-fiscal-
rule.git fiscal-rule  
RUN git clone -b 8.0 --depth=1 http://github.com/Trust-Code/trust-addons.git
trust-addons  
RUN git clone -b 8.0 --depth=1 http://github.com/Trust-Code/server-tools.git
server-tools  
RUN git clone -b 8.0 --depth=1 http://github.com/OCA/bank-payment.git bank-
payment  
RUN git clone -b 8.0 --depth=1 https://github.com/OCA/bank-statement-
import.git bank-statement-import  
RUN git clone -b 8.0 --depth=1 https://github.com/Trust-Code/PySPED.git pysped  
RUN git clone -b master --depth=1 https://github.com/Trust-Code/odoo-
project_scrum.git project-scrum  
RUN git clone -b 8.0 --depth=1 https://github.com/Trust-Code/project.git
project  
RUN git clone -b 8.0 --depth=1 https://github.com/Trust-Code/odoo-brazil-
banking.git odoo-brazil-banking  
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
RUN apt-get --purge remove -y python-pip git && \  
apt-get autoremove -y && \  
apt-get autoclean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /opt/sources/  
  
##### Finalização do Container #####  
VOLUME ["/opt/", "/etc/odoo"]  
CMD ["/usr/bin/supervisord"]  

