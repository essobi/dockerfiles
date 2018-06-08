# DOCKER para odoo 10 de Odoo Community Backports  
FROM ubuntu:16.04  
MAINTAINER Rubén Cabrera Martínez <rcabrera@praxya.com>  
EXPOSE 8069 8071 8072  
# Prueba por si acaso la 10 sólo va en el longpolling  
RUN apt-get update && apt-get install software-properties-common \  
wget \  
-y  
  
RUN add-apt-repository "deb http://apt.postgresql.org/pub/repos/apt xenial-
pgdg main" -y; \  
wget \--quiet -O - https://postgresql.org/media/keys/ACCC4CF8.asc | \  
apt-key add -  
  
RUN apt-get update && apt-get install \  
net-tools \  
git \  
xauth \  
python-pip \  
python-cups \  
python-jinja2 \  
python-unicodecsv \  
python-psycopg2 \  
python-simplejson \  
python-lxml \  
python-imaging \  
python-yaml \  
python-reportlab \  
python-mako \  
python-werkzeug \  
python-dateutil \  
python-unittest2 \  
python-mock \  
python-openid \  
python-docutils \  
python-feedparser \  
python-psutil \  
python-pydot \  
python-vatnumber \  
python-vobject \  
python-xlwt \  
python-ldap \  
python-requests \  
python-decorator \  
python-passlib \  
python-babel \  
python-gevent \  
locales \  
python-webdav \  
python-gdata \  
xfonts-75dpi \  
python-apt \  
xfonts-base \  
python-pyparsing \  
xfonts-utils \  
python-dev \  
python-libxslt1 \  
python-psycopg2 \  
python-geoip \  
python-pybabel \  
python-pyinotify \  
python-tz \  
python-pychart \  
python-openssl \  
python-egenix-mxdatetime \  
python-pypdf \  
python-babel \  
python-zsi \  
postgresql-client-9.6 \  
python-pypdf2 \  
node-clean-css \  
node-less \  
-y  
  
# Pone trusty pero estamos usando la imagen de xenial  
#RUN apt-get
deb=https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.1/wkhtmltox-0.12.1_linux-
trusty-amd64.deb  
RUN wget
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.1/wkhtmltox-0.12.1_linux-
trusty-amd64.deb  
RUN dpkg -i wkhtmltox-0.12.1_linux-trusty-amd64.deb  
  
# TODO:  
# Instalar locale aquí  
  
RUN pip install \  
openupgradelib \  
odoorpc \  
unidecode \  
zeep \  
pandas \  
psycogreen \  
xlrd \  
ofxparse \  
cssutils \  
twilio \  
zklib \  
backports.functools_lru_cache \  
bokeh \  
dbfpy  
RUN mkdir /opt/odoo; mkdir /var/log/odoo; mkdir /var/lib/odoo; mkdir
/opt/repos && mkdir /opt/repos/oca  
RUN useradd \--home /opt/odoo \--shell /bin/bash odoo  
RUN chown -R odoo:odoo /opt/odoo; chown -R odoo:odoo /var/lib/odoo; \  
chown -R odoo:odoo /var/log/odoo; chown -R odoo:odoo /opt/repos  
# Con lo siguiente, cambiamos al usuario odoo y el path donde ejecuta los  
# comandos que se indiquen después.  
USER odoo  
WORKDIR /opt/odoo  
RUN git clone \--branch 10.0 \--depth 1 https://github.com/oca/ocb.git
/opt/odoo  
# Aquí van los repos oca  
WORKDIR /opt/repos/oca  
RUN git clone \--branch 10.0 \--depth 1 https://github.com/oca/stock-
logistics-workflow.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/account-financial-
reporting.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/server-tools.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/web.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/reporting-
engine.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/partner-
contact.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/website.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/sale-workflow.git;
\  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/stock-logistics-
warehouse.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/stock-logistics-
barcode.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/social.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/rma.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/account-
payment.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/account-financial-
tools.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/account-
invoicing.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/purchase-
workflow.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/project.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/product-
variant.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/product-
attribute.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/pos.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/manufacture.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/management-
system.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/knowledge.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/hr.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/e-commerce.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/crm.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/contract.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/commission.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/bank-statement-
reconcile.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/bank-statement-
import.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/bank-payment.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/account-fiscal-
rule.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/account-invoice-
reporting.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/account-
closing.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/account-
budgeting.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/account-
analytic.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/operating-unit.git;
\  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/stock-logistics-
transport.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/hr-timesheet.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/event.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/intrastat.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/sale-financial.git;
\  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/stock-logistics-
tracking.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/sale-reporting.git;
\  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/purchase-
reporting.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/project-
reporting.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/manufacture-
reporting.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/account-
consolidation.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/website-cms.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/l10n-spain.git; \  
git clone \--branch 10.0 \--depth 1 https://github.com/oca/margin-analysis.git  
# Repositorios abiertos qu eno son de la oca ni de Praxya  
# TODO  
# TODO:  
# Repos de praxya (ya no son de instancia)  
# No disponibles todavía para la 10  
# Configuración  
USER root  
RUN mkdir /opt/config  
COPY ./odoo-server.conf /opt/config/odoo-server.conf  
ENV OPENERP_SERVER /opt/config/odoo-server.conf  
  
RUN chown -R odoo:odoo /opt/config  
# Extra-addons is where odoo10 places user installed addons  
#RUN mkdir -p /mnt/extra-addons \  
#&& chown -R odoo /mnt/extra-addons  
RUN sed -i '/^#.*Storage/s/^#//' /etc/systemd/journald.conf  
RUN mkdir -p /var/lib/odoo \  
&& chown -R odoo /var/lib/odoo  
VOLUME ["/var/lib/odoo"]  
COPY ./entrypoint.sh /opt/entrypoint.sh  
RUN chown -R odoo:odoo /opt/entrypoint.sh  
RUN ["chmod", "+x", "/opt/entrypoint.sh"]  
  
USER odoo  
# Metemos el fichero de configuración sin los valores a pasar como  
# variable y luego añadimos al final las variables, usando valores por
defecto:  
# ${variable:-word} indicates that if variable is set then the result will be  
# that value. If variable is not set then word will be the result.  
# ${variable:+word} indicates that if variable is set then word will be the  
# result, otherwise the result is the empty string.  
# Pegar fichero de configuración  
# Introducción de variables en el .conf  
#RUN echo 'db_user = '${ODOO_DB_USER:-odoo} >> /opt/config/odoo-server.conf; \  
#echo 'log_handler = '${LOG_HANDLER:-"[':INFO']"} >> /opt/config/odoo-
server.conf; \  
#echo 'log_level = '${LOG_LEVEL:-info} >> /opt/config/odoo-server.conf; \  
#echo 'log_db = '${LOG_DB:-False} >> /opt/config/odoo-server.conf; \  
#echo 'data_dir = '${DATA_DIR:-"/var/lib/odoo"} >> /opt/config/odoo-
server.conf  
# TODO: Crear un volumen para tener logs persistentes (!)  
# La variable auto_reload no se está metiendo.  
#RUN echo 'logfile = '${LOGFILE:-"/var/log/odoo/odoo-server.log"} >>
/opt/config/odoo-server.conf; \  
#echo 'logrotate = '${LOGROTATE:-True} >> /opt/config/odoo-server.conf; \  
#echo 'csv_internal_sep = '${CSV_INTERNAL_SEP:-";"} >> /opt/config/odoo-
server.conf; \  
#echo 'admin_passwd = '${ADMIN_PASSWD:-admin} >> /opt/config/odoo-server.conf;
\  
#echo 'db_port = '${DB_PORT:-5432} >> /opt/config/odoo-server.conf; \  
#echo 'db_user = '${DB_USER:-odoo} >> /opt/config/odoo-server.conf; \  
#echo 'db_password = '${DB_PASSWORD:-odoo} >> /opt/config/odoo-server.conf; \  
#echo 'db_template = '${DB_TEMPLATE:-template1} >> /opt/config/odoo-
server.conf; \  
#echo 'db_name = '${DB_NAME:-False} >> /opt/config/odoo-server.conf; \  
#echo 'db_maxconn = '${DB_MAXCONN:-64} >> /opt/config/odoo-server.conf  
#RUN echo 'dbfilter = '${DBFILTER:-"^%d"} >> /opt/config/odoo-server.conf  
#RUN echo 'db_maxconn = '${DB_MAXCONN:-64} >> /opt/config/odoo-server.conf; \  
#echo 'debug_mode = '${DEBUG_MODE:-False} >> /opt/config/odoo-server.conf; \  
#echo 'email_from = '${EMAIL_FROM:-False} >> /opt/config/odoo-server.conf; \  
#echo 'limit_memory_hard = '${LIMIT_MEMORY_HARD:-2684354560} >>
/opt/config/odoo-server.conf; \  
#echo 'limit_memory_soft = '${LIMIT_MEMORY_SOFT:-2147483648} >>
/opt/config/odoo-server.conf; \  
#echo 'limit_request = '${LIMIT_REQUEST:-8192} >> /opt/config/odoo-
server.conf; \  
#echo 'limit_time_cpu = '${LIMIT_TIME_CPU:-60} >> /opt/config/odoo-
server.conf; \  
#echo 'limit_time_real = '${LIMIT_TIME_REAL:-120} >> /opt/config/odoo-
server.conf; \  
#echo 'list_db = '${LIST_DB:-True} >> /opt/config/odoo-server.conf  
# Ojo a esta variable porque este es el puerto a exponer en odoo 10,  
# si no me equivoco.  
#RUN echo 'longpolling_port = '${LONGPOLLING_PORT:-8072} >> /opt/config/odoo-
server.conf; \  
#echo 'max_cron_threads = '${MAX_CRON_THREADS:-2} >> /opt/config/odoo-
server.conf; \  
#echo 'osv_memory_age_limit = '${OSV_MEMORY_AGE_LIMIT:-1} >> /opt/config/odoo-
server.conf; \  
#echo 'osv_memory_count_limit = '${OSV_MEMORY_COUNT_LIMIT:-False} >>
/opt/config/odoo-server.conf; \  
#echo 'pg_path = '${PG_PATH:-None} >> /opt/config/odoo-server.conf; \  
#echo 'pidfile = '${PIDFILE:-None} >> /opt/config/odoo-server.conf; \  
#echo 'proxy_mode = '${PROXY_MODE:-False} >> /opt/config/odoo-server.conf; \  
#echo 'reportgz = '${REPORTGZ:-False} >> /opt/config/odoo-server.conf; \  
#echo 'secure_cert_file = '${SECURE_CERT_FILE:-"server.cert"} >>
/opt/config/odoo-server.conf; \  
#echo 'secure_pkey_file = '${SECURE_pkey_FILE:-"server.pkey"} >>
/opt/config/odoo-server.conf; \  
#echo 'server_wide_modules = '${SERVER_WIDE_MODULES:-None} >>
/opt/config/odoo-server.conf; \  
#echo 'smtp_password = '${SMTP_PASSWORD:-False} >> /opt/config/odoo-
server.conf; \  
#echo 'smtp_port = '${SMTP_PORT:-25} >> /opt/config/odoo-server.conf; \  
#echo 'smtp_server = '${SMTP_SERVER:-localhost} >> /opt/config/odoo-
server.conf; \  
#echo 'smtp_ssl = '${SMTP_SSL:-False} >> /opt/config/odoo-server.conf; \  
#echo 'smtp_user = '${SMTP_USER:-False} >> /opt/config/odoo-server.conf; \  
#echo 'syslog = '${SYSLOG:-False} >> /opt/config/odoo-server.conf; \  
#echo 'test_commit = '${TEST_COMMIT:-False} >> /opt/config/odoo-server.conf; \  
#echo 'test_enable = '${TEST_ENABLE:-False} >> /opt/config/odoo-server.conf; \  
#echo 'test_file = '${TEST_FILE:-False} >> /opt/config/odoo-server.conf; \  
#echo 'test_report_directory = '${TEST_REPORT_DIRECTORY:-False} >>
/opt/config/odoo-server.conf; \  
#echo 'timezone = '${TIMEZONE:-False} >> /opt/config/odoo-server.conf; \  
#echo 'translate_modules = '${TRANSLATE_MODULES:-"['all']"} >>
/opt/config/odoo-server.conf; \  
#echo 'unaccent = '${UNACCENT:-True} >> /opt/config/odoo-server.conf; \  
#echo 'without_demo = '${WITHOUT_DEMO:-True} >> /opt/config/odoo-server.conf;
\  
#echo 'workers = '${WORKERS:-0} >> /opt/config/odoo-server.conf; \  
#echo 'xmlrpc = '${XMLRPC:-True} >> /opt/config/odoo-server.conf; \  
#echo 'xmlrpc_port = '${XMLRPC_PORT:-8069} >> /opt/config/odoo-server.conf; \  
#echo 'xmlrpcs = '${XMLRPCS:-True} >> /opt/config/odoo-server.conf; \  
#echo 'xmlrpcs_port = '${XMLRPCS_PORT:-8071} >> /opt/config/odoo-server.conf;
\  
#echo 'db_host = '${DB_HOST:-db} >> /opt/config/odoo-server.conf;  
#ENTRYPOINT /opt/odoo/odoo-bin --config=/opt/config/odoo-server.conf  
ENTRYPOINT ["/opt/entrypoint.sh"]  
CMD ["/opt/odoo/odoo-bin"]  

