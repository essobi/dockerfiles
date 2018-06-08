FROM debian:jessie  
  
MAINTAINER Andrei Poenaru <andrei.poenaru@gmail.com>  
  
# linkr version  
ARG version=master  
  
# Build configuration  
ARG admin_user=admin  
ARG admin_pass=password  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Dependencies  
RUN set -x && \  
apt-get -qq update && \  
apt-get -y install curl git python-pip libmysqlclient-dev python-dev apache2
libapache2-mod-wsgi && \  
pip install virtualenv && \  
echo 'deb http://ftp.utexas.edu/dotdeb/ jessie all' >>
/etc/apt/sources.list.d/dotdeb.list && \  
echo 'deb-src http://ftp.utexas.edu/dotdeb/ jessie all' >>
/etc/apt/sources.list.d/dotdeb.list && \  
curl -s https://www.dotdeb.org/dotdeb.gpg | apt-key add - && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get -y install nodejs redis-server && \  
git clone https://github.com/LINKIWI/linkr.git /linkr && \  
cd /linkr && \  
git checkout "$version"  
  
# Env setup  
COPY apache.conf /etc/apache2/sites-available/linkr.conf  
RUN set -x && \  
a2dissite 000-default.conf && \  
a2ensite linkr.conf && \  
a2enmod wsgi && \  
cd /linkr/ && \  
virtualenv env && \  
. env/bin/activate && \  
pip install -r requirements.txt && \  
npm install --quiet  
  
# Configuration  
COPY config/ /config/  
COPY copy_config.sh /linkr/copy_config.sh  
COPY check_db.sh /linkr/check_db.sh  
RUN cd /linkr/ && \  
. env/bin/activate && \  
mkdir /data && \  
bash copy_config.sh && \  
rm copy_config.sh && \  
NODE_ENV=production npm run build && \  
echo '' > linkr_setup_input.txt && \  
echo '' >> linkr_setup_input.txt && \  
echo "$admin_user" >> linkr_setup_input.txt && \  
echo "$admin_pass" >> linkr_setup_input.txt && \  
echo "$admin_pass" >> linkr_setup_input.txt && \  
cat linkr_setup_input.txt | python linkr_setup.py && \  
rm linkr_setup_input.txt && \  
chown www-data:www-data /data && \  
chown www-data:www-data /data/linkr.db && \  
cp /data/linkr.db /linkr/linkr_new.db  
  
# Remove unneeded packages  
RUN set -x && \  
apt-get remove -y curl && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* && \  
set +x  
  
VOLUME ["/data"]  
EXPOSE 80  
COPY startup.sh /startup.sh  
CMD ["/startup.sh"]  
  

