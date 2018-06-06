FROM python:2.7.14  
  
LABEL maintainer="Haiwei Liu <carllhw@gmail.com>"  
  
RUN groupadd -r odoo && useradd -r -g odoo odoo  
  
ENV POSTGRESQL_VERSION 9.5  
  
RUN set -x \  
&& echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" >
/etc/apt/sources.list.d/pgdg.list \  
&& wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-
key add \- \  
&& apt-get update \  
&& apt-get install -y \--no-install-recommends \  
libldap2-dev \  
libsasl2-dev \  
node-less \  
postgresql-client-$POSTGRESQL_VERSION \  
ttf-wqy-zenhei \  
unzip \  
&& curl -o wkhtmltox.deb -SL
http://nightly.odoo.com/extra/wkhtmltox-0.12.1.2_linux-jessie-amd64.deb \  
&& echo '40e8b906de658a2221b15e4e8cd82565a47d7ee8 wkhtmltox.deb' | sha1sum -c
\- \  
&& dpkg --force-depends -i wkhtmltox.deb \  
&& apt-get -y install -f \--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* wkhtmltox.deb  

