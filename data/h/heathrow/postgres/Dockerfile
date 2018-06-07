FROM postgres:9.3.18  
  
RUN localedef -i ja_JP -c -f UTF-8 -A /usr/share/locale/locale.alias
ja_JP.UTF-8  
ENV LANG ja_JP.utf8  
  
RUN apt-get -qq update && \  
apt-get -qq -y install \  
postgis \  
postgresql-9.3-postgis-2.3 \  
libpq-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
mkdir -p /etc/service/psql && \  
touch /etc/service/psql/run

