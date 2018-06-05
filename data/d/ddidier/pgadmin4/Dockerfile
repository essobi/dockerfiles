#  
# ddidier/pgadmin4  
#  
# A Docker image for pgAdmin 4.  
#  
# docker build -t ddidier/pgadmin4 .  
FROM httpd:2.4.27  
MAINTAINER David DIDIER  
  
ENV PGADMIN_VERSION=1.6  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends build-essential ca-certificates
libapache2-mod-wsgi python-dev python-pip wget \  
&& sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main"
> /etc/apt/sources.list.d/postgres.list' \  
&& wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-
key add - \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends libpq-dev \  
&& pip install --upgrade pip \  
&& pip install
"https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v${PGADMIN_VERSION}/pip/pgadmin4-${PGADMIN_VERSION}-py2.py3-none-
any.whl" \  
&& apt-get autoremove -y \  
&& rm -rf /var/cache/* \  
&& rm -rf /var/lib/apt/lists/*  
  
# For development  
# COPY files/pgadmin4-${PGADMIN_VERSION}-py2.py3-none-any.whl
/tmp/pgadmin4-${PGADMIN_VERSION}-py2.py3-none-any.whl  
# RUN pip install "/tmp/pgadmin4-${PGADMIN_VERSION}-py2.py3-none-any.whl"  
COPY files/usr/local/apache2/conf/httpd.conf /usr/local/apache2/conf/  
COPY files/usr/local/bin/docker-entrypoint /usr/local/bin/  
COPY files/usr/local/lib/python2.7/dist-
packages/pgadmin4/config-${PGADMIN_VERSION}-template.py
/usr/local/lib/python2.7/dist-packages/pgadmin4/  
  
RUN chown root:www-data /usr/local/apache2/conf/httpd.conf \  
&& chmod 644 /usr/local/apache2/conf/httpd.conf \  
\  
&& chown root:root /usr/local/bin/docker-entrypoint \  
&& chmod 755 /usr/local/bin/docker-entrypoint \  
\  
&& mkdir /data \  
&& chown daemon:daemon /data \  
&& chmod 755 /data  
  
# Enviroment variables that may be overridden with their default:  
#  
# DEFAULT_SERVER_HOST = localhost  
# DEFAULT_SERVER_PORT = 5050  
# SQLITE_TIMEOUT = 500  
# MAIL_SERVER = localhost  
# MAIL_PORT = 25  
# MAIL_USE_SSL = False  
# MAIL_USE_TLS = False  
# MAIL_USERNAME =  
# MAIL_PASSWORD =  
# MAIL_DEBUG = False  
# UPGRADE_CHECK_ENABLED = True  
#  
# PGADMIN_SETUP_EMAIL = admin@example.com  
# PGADMIN_SETUP_PASSWORD = changeme  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint"]  

