FROM odoo:9  
MAINTAINER Pablo González <pablodgonzalez@gmail.com>  
  
USER root  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends\  
build-essential \  
git \  
libcups2-dev \  
libssl-dev \  
libffi-dev \  
locales \  
python-dev \  
python-httplib2 \  
python-m2crypto  
  
RUN locale-gen en_US.UTF-8 && update-locale && locale-gen es_AR.UTF-8 &&
update-locale && echo 'LANG="en_US.UTF-8"' > /etc/default/locale  
ENV LANG es_AR.UTF-8  
ENV LANGUAGE es_AR:es:en_US:en  
ENV LC_ALL es_AR.UTF-8  
  
RUN mkdir -p /var/extra-addons \  
&& git clone -b 9.0 https://github.com/OCA/account-closing /var/extra-
addons/OCA/account-closing \  
&& git clone -b 9.0 https://github.com/OCA/account-financial-tools /var/extra-
addons/OCA/account-financial-tools \  
&& git clone -b 9.0 https://github.com/OCA/bank-payment /var/extra-
addons/OCA/bank-payment \  
&& git clone -b 9.0 https://github.com/OCA/connector /var/extra-
addons/OCA/connector \  
&& git clone -b 9.0 https://github.com/OCA/margin-analysis /var/extra-
addons/OCA/margin-analysis \  
&& git clone -b 9.0 https://github.com/OCA/partner-contact /var/extra-
addons/OCA/partner-contact \  
&& git clone -b 9.0 https://github.com/OCA/product-attribute /var/extra-
addons/OCA/product-attribute \  
&& git clone -b 9.0 https://github.com/OCA/reporting-engine /var/extra-
addons/OCA/reporting-engine \  
&& git clone -b 9.0 https://github.com/OCA/sale-workflow /var/extra-
addons/OCA/sale-workflow \  
&& git clone -b 9.0 https://github.com/OCA/server-tools /var/extra-
addons/OCA/server-tools \  
&& git clone -b 9.0 https://github.com/OCA/stock-logistics-barcode /var/extra-
addons/OCA/stock-logistics-barcode \  
&& git clone -b 9.0 https://github.com/OCA/stock-logistics-tracking
/var/extra-addons/OCA/stock-logistics-tracking \  
&& git clone -b 9.0 https://github.com/OCA/stock-logistics-transport
/var/extra-addons/OCA/stock-logistics-transport \  
&& git clone -b 9.0 https://github.com/OCA/stock-logistics-warehouse
/var/extra-addons/OCA/stock-logistics-warehouse \  
&& git clone -b 9.0 https://github.com/OCA/stock-logistics-workflow
/var/extra-addons/OCA/stock-logistics-workflow \  
&& git clone -b 9.0 https://github.com/OCA/web /var/extra-addons/OCA/web \  
&& git clone -b 9.0 https://github.com/OCA/webkit-tools /var/extra-
addons/OCA/webkit-tools \  
&& git clone -b 9.0 https://github.com/ingadhoc/account-financial-tools
/var/extra-addons/ingadhoc/account-financial-tools \  
&& git clone -b 9.0 https://github.com/ingadhoc/account-invoicing /var/extra-
addons/ingadhoc/account-invoicing \  
&& git clone -b 9.0 https://github.com/ingadhoc/account-payment /var/extra-
addons/ingadhoc/account-payment \  
&& git clone -b 9.0 https://github.com/ingadhoc/aeroo_reports /var/extra-
addons/ingadhoc/aeroo_reports \  
&& git clone -b 9.0 https://github.com/ingadhoc/argentina-reporting
/var/extra-addons/ingadhoc/argentina-reporting \  
&& git clone -b 9.0 https://github.com/ingadhoc/argentina-sale /var/extra-
addons/ingadhoc/argentina-sale \  
&& git clone -b 9.0 https://github.com/ingadhoc/miscellaneous /var/extra-
addons/ingadhoc/miscellaneous \  
&& git clone -b 8.0 https://github.com/ingadhoc/odoo-addons /var/extra-
addons/ingadhoc/odoo-addons \  
&& git clone -b 9.0 https://github.com/ingadhoc/odoo-argentina /var/extra-
addons/ingadhoc/odoo-argentina \  
&& git clone -b 9.0 https://github.com/ingadhoc/patches /var/extra-
addons/ingadhoc/patches \  
&& git clone -b 9.0 https://github.com/ingadhoc/reporting-engine /var/extra-
addons/ingadhoc/reporting-engine \  
&& git clone -b 9.0 https://github.com/ingadhoc/stock /var/extra-
addons/ingadhoc/stock  
  
  
RUN chown -R odoo /var/extra-addons \  
&& pip install --upgrade pip setuptools openupgradelib \  
&& pip install -r /var/extra-addons/OCA/partner-contact/requirements.txt \  
&& pip install -r /var/extra-addons/OCA/reporting-engine/requirements.txt \  
&& pip install -r /var/extra-addons/OCA/server-tools/requirements.txt \  
&& pip install -r /var/extra-addons/OCA/stock-logistics-
barcode/requirements.txt \  
&& pip install -r /var/extra-addons/ingadhoc/odoo-argentina/requirements.txt \  
&& pip install -r /var/extra-addons/ingadhoc/patches/requirements.txt \  
&& pip install git+https://github.com/aeroo/aeroolib.git \  
&& chown odoo /usr/local/lib/python2.7/dist-packages/pyafipws/  
  
COPY ./conf/openerp-server.conf /etc/odoo/  
  
USER odoo  
  
CMD ["openerp-server"]

