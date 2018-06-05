FROM debian:jessie  
  
ENV \  
CACTI_VERSION=1.1.28 \  
  
DEBIAN_FRONTEND=noninteractive \  
TERM=xterm \  
  
DB_NAME=cacti \  
DB_USER=cactiuser \  
DB_PASS=cactipassword \  
DB_HOST=localhost \  
DB_PORT=3306 \  
  
RDB_NAME=cacti \  
RDB_USER=cactiuser \  
RDB_PASS=cactipassword \  
RDB_HOST=localhost \  
RDB_PORT=3306 \  
  
BACKUP_RETENTION=7 \  
BACKUP_TIME=0 \  
  
SNMP_COMMUNITY=public \  
REMOTE_POLLER=0 \  
INITIALIZE_DB=0 \  
INITIALIZE_INFLUX=0 \  
TZ=Europe/Berlin  
  
## Install dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends \  
apt-utils \  
apt-transport-https \  
ca-certificates \  
dbconfig-common \  
git \  
perl \  
libapache2-mod-php5 \  
libphp-adodb \  
php5-cli \  
php5-mysql \  
php5-snmp \  
php5-ldap \  
php5-gd \  
php5-gmp \  
rrdtool \  
vim \  
wget \  
mysql-client \  
debconf \  
perl \  
ssl-cert \  
less \  
rsync \  
ssh-client \  
snmp \  
cron \  
python \  
python-simplejson \  
&& rm -rf /var/lib/apt/lists/*  
  
## INSTALL CACTI  
WORKDIR "/tmp"  
RUN wget https://www.cacti.net/downloads/cacti-${CACTI_VERSION}.tar.gz && \  
tar -xf /tmp/cacti-${CACTI_VERSION}.tar.gz -C /tmp && \  
rm -f /tmp/cacti-${CACTI_VERSION}.tar.gz && \  
mv /tmp/cacti-${CACTI_VERSION}/ /cacti  
  
## INSTALL SPINE  
WORKDIR "/tmp"  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
libssl-dev \  
libmysqlclient-dev \  
libsnmp-dev \  
help2man && \  
wget https://www.cacti.net/downloads/spine/cacti-spine-${CACTI_VERSION}.tar.gz
&& \  
tar -xf /tmp/cacti-spine-${CACTI_VERSION}.tar.gz -C /tmp && \  
cd /tmp/cacti-spine-${CACTI_VERSION} && \  
./configure --prefix=/spine && make && make install && \  
chown root:root /spine/bin/spine && \  
chmod +s /spine/bin/spine && \  
rm -rf /tmp/* && \  
apt-get autoremove -y build-essential libssl-dev libmysqlclient-dev libsnmp-
dev help2man  
  
## SETUP CRON  
WORKDIR "/"  
COPY config/crontab /etc/crontab  
# make pam_loginuid.so optional for cron  
# see https://github.com/docker/docker/issues/5663#issuecomment-42550548  
RUN sed -i -e 's/^session.*required.*pam_loginuid.so$/session optional
pam_loginuid.so/' /etc/pam.d/cron  
  
## SERVICE CONFIGS  
WORKDIR "/"  
COPY config/spine.conf /spine/etc  
COPY config/000-default.conf /etc/apache2/sites-available/  
COPY config/config.php /cacti/include  
COPY config /template_configs  
  
## SETTINGS/EXTRAS  
WORKDIR "/"  
COPY templates /templates  
COPY settings /settings  
  
## Start  
WORKDIR "/"  
COPY start.sh /start.sh  
RUN chmod +x /start.sh  
CMD ["/start.sh"]  
  
EXPOSE 80 443

