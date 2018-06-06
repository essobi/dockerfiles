#-- 00 Descarga odoo v8.0 ----  
FROM odoo:8.0  
MAINTAINER jalv  
# based on https://github.com/bmya/docker-odoo-bmya  
#-- 00.01 Configuración ambiente de trabajo -----  
USER root  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -qq && apt-get install -y locales -qq  
RUN echo 'es_AR.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen  
RUN echo 'es_CL.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen  
RUN echo 'es_US.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen  
RUN echo 'C.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen  
RUN dpkg-reconfigure locales && /usr/sbin/update-locale LANG=C.UTF-8  
ENV LANG C.UTF-8  
ENV LANGUAGE C.UTF-8  
ENV LC_ALL C.UTF-8  
#-- 00.02 Preparando Instalador pip y dependencias indispensables --  
RUN apt-get update && apt-get install -y \  
apt-utils \  
ghostscript \  
git \  
python-pip \  
sudo \  
vim  
  
#-- 01 Instalación adoons Localización Chilena y DTE Chile -----  
#-- 01.01 Creación y cambio de directorio de trabajo  
#RUN mkdir -p /mnt/extra-addons  
#el directorio /mnt/extra-addons ya fue creado por odoo, eliminar una vez
depurado  
RUN mkdir -p /opt/odoo/stable-addons/odoo-chile/ \  
&& chown -R odoo /opt/odoo/stable-addons/odoo-chile  
WORKDIR /opt/odoo/stable-addons/odoo-chile/  
  
#-- 01.01.01 Descarga de addons ---  
#RUN git clone -b 8.0 https://github.com/bmya/odoo-argentina.git  
RUN git clone -b 8.0 https://github.com/odoo-chile/account_bank_voucher.git  
RUN git clone -b 8.0 https://github.com/odoo-chile/invoice_printed.git  
RUN git clone -b 8.0 https://github.com/odoo-
chile/l10n_cl_account_vat_ledger.git  
RUN git clone -b 8.0 https://github.com/odoo-chile/l10n_cl_banks_sbif.git  
RUN git clone -b 8.0 https://github.com/odoo-chile/l10n_cl_base_rut.git  
RUN git clone -b 8.0 https://github.com/odoo-chile/l10n_cl_base.git  
RUN git clone -b 8.0 https://github.com/odoo-chile/l10n_cl_chart.git  
RUN git clone -b 8.0 https://github.com/odoo-
chile/l10n_cl_clean_doc_number.git  
RUN git clone -b 8.0 https://github.com/odoo-
chile/l10n_cl_clear_translation.git  
RUN git clone -b 8.0 https://github.com/odoo-chile/l10n_cl_counties.git  
RUN git clone -b 8.0 https://github.com/odoo-chile/l10n_cl_dte_caf.git  
RUN git clone -b 8.0 https://github.com/odoo-chile/l10n_cl_dte_picking.git  
RUN git clone -b 8.0 https://github.com/odoo-chile/l10n_cl_dte.git  
RUN git clone -b 8.0 https://github.com/odoo-
chile/l10n_cl_financial_indicators.git  
RUN git clone -b 8.0 https://github.com/odoo-chile/l10n_cl_hr_payroll.git  
RUN git clone -b 8.0 https://github.com/odoo-chile/l10n_cl_invoice.git  
RUN git clone -b 8.0 https://github.com/odoo-
chile/l10n_cl_partner_activities.git  
RUN git clone -b 8.0 https://github.com/odoo-chile/l10n_cl_pos_basic_users.git  
RUN git clone -b 8.0 https://github.com/odoo-
chile/l10n_cl_pos_credit_card_voucher.git  
RUN git clone -b 8.0 https://github.com/odoo-chile/l10n_cl_toponyms.git  
RUN git clone -b 8.0 https://github.com/odoo-chile/l10n_cl_vat.git  
RUN git clone -b 8.0 https://github.com/odoo-chile/webservices_generic.git  
  
#-- 01.02 Instalación de dependencias ---  
#-- 01.02.01 Requerimientos addons odoo-chile ---  
RUN pip install BeautifulSoup \  
urllib3  
  
#RUN pip install cchardet  
#RUN pip install dicttoxml  
#RUN pip install elaphe  
#RUN pip install hashlib \  
#RUN pip install lxml  
#RUN pip install signxml  
#RUN pip install xmltodict  
#-- 99.00 Copia de archivos configuración del servidor a carpeta
correspondiente  
COPY ./entrypoint.sh / \  
./openerp-server.conf /etc/odoo/  
  
USER odoo

