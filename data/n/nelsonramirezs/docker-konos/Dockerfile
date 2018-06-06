FROM nelsonramirezs/odoo9:latest  
MAINTAINER Nelson Ramirez <info@konos.cl>  
  
  
USER root  
  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -qq && apt-get install -y locales -qq  
RUN echo 'es_CL.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen  
RUN echo 'es_US.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen  
RUN echo 'C.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen  
RUN dpkg-reconfigure locales && /usr/sbin/update-locale LANG=C.UTF-8  
ENV LANG C.UTF-8  
ENV LANGUAGE C.UTF-8  
ENV LC_ALL C.UTF-8  
RUN apt-get update && apt-get install -y python-pip git vim  
RUN apt-get install -y ghostscript && \  
apt-get install -y python-gevent && \  
apt-get install -y python-dev freetds-dev build-essential && \  
apt-get install -y python-matplotlib font-manager && \  
apt-get install -y swig libffi-dev libssl-dev python-httplib2 mercurial && \  
apt-get install -y libxml2-dev libxmlsec1-dev libxslt-dev python-dev
lib32z1-dev liblz-dev && \  
apt-get install -y swig libssl-dev && \  
apt-get install -y libcups2-dev && \  
apt-get install -y libxslt1-dev python-lxml python-openssl python-defusedxml
&& \  
apt-get install -y python-sqlalchemy && \  
apt-get install -y unixodbc-dev unixodbc-bin unixodbc && \  
apt-get install -y postgis  
  
RUN apt-get -q update && apt-get -yq install --no-install-recommends gis-devel
\  
python-scipy \  
python-matplotlib \  
python-shapely  
  
RUN pip install --upgrade pip  
RUN pip install certifi  
  
# dte implementation  
RUN pip install xmltodict  
RUN pip install dicttoxml  
RUN pip install elaphe  
RUN pip install pdf417gen  
#RUN pip install hashlib  
RUN pip install cchardet  
RUN pip install suds  
RUN pip install urllib3  
RUN pip install SOAPpy  
RUN pip install cryptography  
RUN pip install M2Crypto  
RUN pip install --upgrade setupext-pip  
RUN pip install signxml==1.0.1  
#RUN pip install textwrap  
#RUN pip install cStringIO  
RUN pip install pysftp==0.2.8  
RUN pip install urllib3==1.7.1  
RUN pip install requests==2.6.0  
RUN pip install xlsxwriter  
RUN pip install dropbox  
RUN pip install xlrd  
  
#Jarsa Libs  
RUN pip install simplejson  
RUN pip install geojson  
RUN pip install geopy  
RUN pip install geographiclib  
RUN pip install sodapy  
RUN pip install num2words  
RUN pip install pyBarcode  
  
# oca reports  
RUN pip install xlwt  
  
# Asana  
RUN pip install inflect  
RUN pip install requests[security]  
  
# create directories for repos  
RUN mkdir -p /opt/odoo/stable-addons/oca  
RUN mkdir -p /opt/odoo/stable-addons/konos  
RUN mkdir -p /opt/odoo/stable-addons/otros  
RUN mkdir -p /opt/odoo/stable-addons/bmya/odoo-chile  
RUN mkdir -p /opt/odoo/stable-addons/konos/odoo-colombia  
RUN mkdir -p /opt/odoo/.filelocal/odoo  
RUN mkdir -p /var/lib/odoo/backups/synced  
  
# update openerp-server.conf file (todo: edit with "sed")  
COPY ./openerp-server.conf /etc/odoo/  
RUN chown odoo /etc/odoo/openerp-server.conf  
RUN chmod 644 /etc/odoo/openerp-server.conf  
RUN chown -R odoo /opt/odoo  
RUN chown -R odoo /opt/odoo/stable-addons  
RUN chown -R odoo /mnt/extra-addons  
RUN chown -R odoo /var/lib/odoo  
  
# oca partner contacts  
RUN pip install unicodecsv  
  
# aeroo direct print  
RUN pip install git+https://github.com/aeroo/aeroolib.git@master  
#RUN pip install git+https://github.com/ingadhoc/aeroo_reports.git@9.0  
RUN pip install pycups==1.9.68  
  
RUN pip install xlsxwriter  
RUN pip install mercadopago  
  
RUN pip install pyzk  
  
WORKDIR /opt/odoo/stable-addons/bmya/odoo-chile/  
  
RUN git clone -b 9.0 https://github.com/dansanti/l10n_cl_banks_sbif.git \  
&& git clone -b konos https://github.com/KonosCL/l10n_cl_invoice.git \  
&& git clone -b 9.0 https://github.com/dansanti/l10n_cl_dte.git \  
&& git clone -b 9.0 https://github.com/dansanti/l10n_cl_stock_picking.git \  
&& git clone -b 9.0 https://github.com/KonosCL/l10n_cl_hr_payroll.git \  
&& git clone -b 9.0 https://github.com/dansanti/l10n_cl_counties.git \  
&& git clone -b 9.0 https://github.com/dansanti/l10n_cl_partner_activities.git
\  
&& git clone -b 9.0 https://github.com/dansanti/l10n_cl_base_rut.git \  
&& git clone -b 9.0 https://github.com/odoo-
chile/l10n_cl_financial_indicators.git \  
&& git clone -b 9.0 https://github.com/dansanti/base_state_ubication.git \  
&& git clone -b 9.0 https://github.com/dansanti/user_signature_key.git \  
&& git clone -b 9.0 https://github.com/dansanti/webservices_generic.git \  
&& git clone -b master https://github.com/dansanti/l10n_cl_dte_factoring.git \  
&& git clone -b 9.0 https://github.com/dansanti/global_discount.git \  
&& git clone -b 9.0 https://github.com/dansanti/l10n_cl_dte_point_of_sale.git
\  
&& git clone -b 9.0 https://github.com/dansanti/l10n_cl_libro_compra_venta.git
\  
&& git clone -b 9.0 https://github.com/dansanti/l10n_cl_dte_caf.git  
  
  
  
WORKDIR /opt/odoo/stable-addons/konos/odoo-colombia/  
  
RUN git clone -b 9.0 https://github.com/KonosCL/l10n-colombia.git \  
&& git clone -b master https://github.com/KonosCL/l10n_co_res_partner.git \  
&& git clone -b master https://github.com/KonosCL/l10n_co_tax_extension.git  
  
WORKDIR /opt/odoo/stable-addons/oca/  
  
RUN git clone -b 9.0 https://github.com/OCA/server-tools.git \  
&& git clone -b 9.0 https://github.com/OCA/crm.git \  
&& git clone -b 9.0 https://github.com/OCA/pos.git \  
&& git clone -b 9.0 https://github.com/OCA/e-commerce.git \  
&& git clone -b 9.0 https://github.com/OCA/web.git \  
&& git clone -b 9.0 https://github.com/OCA/sale-workflow.git \  
&& git clone -b 9.0 https://github.com/OCA/bank-statement-reconcile.git \  
&& git clone -b 9.0 https://github.com/OCA/stock-logistics-warehouse.git \  
&& git clone -b 9.0 https://github.com/OCA/account-invoicing.git \  
&& git clone -b 9.0 https://github.com/OCA/account-financial-tools.git \  
&& git clone -b 9.0 https://github.com/OCA/account-payment.git \  
&& git clone -b 9.0 https://github.com/OCA/product-attribute.git \  
&& git clone -b 9.0 https://github.com/OCA/account-financial-reporting.git \  
&& git clone -b 9.0 https://github.com/OCA/geospatial.git \  
&& git clone -b 9.0 https://github.com/OCA/stock-logistics-workflow.git \  
&& git clone -b 9.0 https://github.com/OCA/bank-payment.git  
  
WORKDIR /opt/odoo/stable-addons/otros/  
  
RUN git clone -b 9.0 https://github.com/KonosCL/account-payment.git \  
&& git clone -b 9.0 https://github.com/ingadhoc/account-invoicing.git \  
&& git clone -b 9.0 https://github.com/ingadhoc/account-financial-tools.git \  
&& git clone -b 9.0 https://github.com/ingadhoc/sale.git \  
&& git clone -b 9.0 https://github.com/ingadhoc/product.git \  
&& git clone -b 9.0 https://github.com/dansanti/payment_webpay.git \  
&& git clone -b 9.0 https://github.com/KonosCL/payment_mercadopago.git \  
&& git clone -b 9.0 https://github.com/KonosCL/odoo-ifrs.git \  
&& git clone -b master https://github.com/KonosCL/report_xlsx.git \  
&& git clone -b 9.0 https://github.com/KonosCL/auto_backup.git \  
&& git clone -b 9.0 https://github.com/KonosCL/addons-konos.git \  
&& git clone -b 9.0 https://github.com/KonosCL/konos-chile.git \  
&& git clone -b 9.0 https://github.com/KonosCL/tko-addons.git \  
&& git clone -b 9.0 https://github.com/KonosCL/themes.git \  
&& git clone -b 9.0 https://github.com/KonosCL/CybroAddons.git \  
&& git clone -b 9.0 https://github.com/KonosCL/aeroo_reports.git  
  
RUN chown -R odoo:odoo /opt/odoo/stable-addons  
WORKDIR /opt/odoo/stable-addons/  
  
RUN git clone -b 9.0 https://github.com/KonosCL/aeroo_reports.git  
  
## Clean apt-get (copied from odoo)  
RUN apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Change default aeroo host name to match docker name  
RUN sed -i "s/localhost/aeroo/" /opt/odoo/stable-
addons/aeroo_reports/report_aeroo/docs_client_lib.py  
RUN sed -i "s/localhost/aeroo/" /opt/odoo/stable-
addons/aeroo_reports/report_aeroo/installer.py  
RUN sed -i "s/localhost/aeroo/" /opt/odoo/stable-
addons/aeroo_reports/report_aeroo/report_aeroo.py  
  
# Set default user when running the container  
USER odoo  

