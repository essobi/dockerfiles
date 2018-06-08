FROM odoo:8  
ENV ODOO_DB_INSTANCE_DB=odoo_instance  
USER root  
RUN apt-get update && apt-get install -y --force-yes \  
python-dev \  
libssl-dev \  
python-openssl \  
build-essential \  
libcups2-dev \  
python-pip \  
curl \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN pip install genshi==0.6.1
http://launchpad.net/aeroolib/trunk/1.0.0/+download/aeroolib.tar.gz
BeautifulSoup geopy==0.95.1 odfpy werkzeug==0.8.3 http pyPdf xlrd pycups suds
M2Crypto  
  
#installing required pyafipws module  
RUN curl -L https://github.com/reingart/pyafipws/tarball/master | tar -zx &&
mv *pyafipws* pyafipws-master \  
&& cd pyafipws-master && pip install -r requirements.txt && pip install .  
  
ADD ./config/openerp-server.conf /etc/odoo/openerp-server.conf  
  
ADD ./modules_repos/aeroo_reports /mnt/extra-addons/aeroo_reports  
ADD ./modules_repos/odoo-addons /mnt/extra-addons/odoo-addons  
ADD ./modules_repos/odoo-argentina /mnt/extra-addons/odoo-argentina  
  
EXPOSE 8069  
USER odoo  
  

