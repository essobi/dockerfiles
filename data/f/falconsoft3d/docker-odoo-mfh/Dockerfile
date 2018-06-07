FROM falconsoft3d/odoo:t1  
MAINTAINER Nelson Ramirez <info@konos.cl>  
# based on https://github.com/bmya/docker-odoo-adhoc  
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
apt-get install -y python-dev freetds-dev && \  
apt-get install -y python-matplotlib font-manager && \  
apt-get install -y swig libffi-dev libssl-dev python-httplib2 mercurial && \  
apt-get install -y libxml2-dev libxslt-dev python-dev lib32z1-dev liblz-dev &&
\  
apt-get install -y swig libssl-dev && \  
apt-get install -y libcups2-dev && \  
apt-get install -y libxslt1-dev python-lxml python-openssl python-defusedxml
&& \  
apt-get install -y python-sqlalchemy && \  
apt-get install -y unixodbc-dev unixodbc-bin unixodbc  
  
RUN pip install certifi  
  
# dte implementation  
RUN pip install xmltodict  
RUN pip install dicttoxml==1.7.4  
RUN pip install elaphe  
#RUN pip install hashlib  
RUN pip install cchardet  
RUN pip install suds  
RUN pip install urllib3  
RUN pip install SOAPpy  
RUN pip install M2Crypto  
RUN pip install --upgrade setupext-pip  
RUN pip install signxml==1.0.1  
#RUN pip install textwrap  
#RUN pip install cStringIO  
RUN pip install pysftp==0.2.8  
RUN pip install urllib3==1.7.1  
RUN pip install requests==2.6.0  
RUN pip install xlsxwriter  
  
# oca reports  
RUN pip install xlwt  
  
# create directories for repos  
RUN mkdir -p /opt/odoo/stable-addons/oca  
RUN mkdir -p /opt/odoo/stable-addons/bmya/odoo-chile  
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
RUN pip install pycups==1.9.68  
  
RUN pip install xlsxwriter  
RUN pip install mercadopago  
  
WORKDIR /opt/odoo/stable-addons/bmya/odoo-chile/  
  
RUN git clone -b 9.0 https://github.com/dansanti/l10n_cl_banks_sbif.git \  
&& git clone -b 9.0 https://github.com/dansanti/l10n_cl_invoice.git \  
&& git clone -b 9.0 https://github.com/dansanti/l10n_cl_dte.git \  
&& git clone -b 9.0 https://github.com/dansanti/l10n_cl_stock_picking.git \  
&& git clone -b 9.0 https://github.com/dansanti/l10n_cl_dte_point_of_sale.git
\  
&& git clone -b 9.0 https://github.com/dansanti/l10n_cl_libro_compra_venta.git
\  
&& git clone -b 9.0 https://github.com/dansanti/l10n_cl_dte_caf.git \  
&& git clone -b 9.0 https://github.com/dansanti/l10n_cl_counties.git \  
&& git clone -b 9.0 https://github.com/dansanti/l10n_cl_partner_activities.git
\  
&& git clone -b 9.0 https://github.com/dansanti/l10n_cl_base_rut.git \  
&& git clone -b 9.0 https://github.com/dansanti/global_discount \  
&& git clone -b 9.0 https://github.com/dansanti/base_state_ubication.git \  
&& git clone -b 9.0 https://github.com/dansanti/user_signature_key.git \  
&& git clone -b 9.0 https://github.com/dansanti/webservices_generic.git \  
&& git clone -b 9.0 https://github.com/odoo-chile/l10n_cl_hr_payroll.git \  
&& git clone -b 9.0 https://github.com/odoo-
chile/l10n_cl_financial_indicators.git \  
&& git clone -b 9.0 https://github.com/odoo-
chile/l10n_cl_account_vat_ledger.git  
  
WORKDIR /opt/odoo/stable-addons/oca/  
  
RUN git clone -b 9.0 https://github.com/OCA/server-tools.git \  
&& git clone -b 9.0 https://github.com/OCA/crm.git \  
&& git clone -b 9.0 https://github.com/OCA/pos.git \  
&& git clone -b 9.0 https://github.com/OCA/e-commerce.git \  
&& git clone -b 9.0 https://github.com/OCA/web.git \  
&& git clone -b 9.0 https://github.com/OCA/bank-statement-reconcile.git \  
&& git clone -b 9.0 https://github.com/OCA/account-invoicing.git \  
&& git clone -b 9.0 https://github.com/ingadhoc/account-payment.git \  
&& git clone -b 9.0 https://github.com/OCA/account-financial-tools.git  
  
  
  
RUN chown -R odoo:odoo /opt/odoo/stable-addons  
WORKDIR /opt/odoo/stable-addons/  
  
RUN git clone -b 9.0 https://github.com/KonosCL/aeroo_reports.git \  
&& git clone -b 9.0 https://github.com/KonosCL/payment_mercadopago.git \  
&& git clone -b 9.0 https://github.com/KonosCL/odoo-ifrs.git \  
&& git clone -b master https://github.com/KonosCL/report_xlsx.git \  
&& git clone -b 9.0 https://github.com/KonosCL/auto_backup.git  
  
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

