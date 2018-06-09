FROM pataquets/supervisor  
  
#############################################################################  
### cloe_run dependencies  
#############################################################################  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
daemontools \  
inotify-tools \  
moreutils \  
python-pip  
  
#############################################################################  
### autossh  
#############################################################################  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install autossh \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
#############################################################################  
### php5-cli, modules and mail  
#############################################################################  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
php5-cli \  
php5-curl \  
php5-imap \  
php5-mcrypt \  
php5-mongo \  
php5-mysql \  
msmtp-mta \  
libmagic-dev \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
echo 'sendmail_path = "/usr/lib/sendmail -t -f no-reply@talentclue.com"' >>
/etc/php5/mods-available/referup-mail.ini ; \  
php5enmod \  
mcrypt referup-mail  
  
#############################################################################  
### wkhtmltopdf  
#############################################################################  
### Ubuntu repositories' package depends on an X-Window server installed.  
### We use wkhtmltopdf.org binary download.  
  
# Wkhtmltopdf PHP class allows you to run the binary program under a  
# fake X Window server (Xvfb)  
# Also install wkhtmltopdf standalone .deb package dependencies  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y \  
libjpeg-turbo8 \  
libxrender1 \  
fontconfig \  
fonts-dejavu \  
fonts-droid \  
xfonts-75dpi \  
xvfb \  
curl \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Wkhtmltopdf PHP class expects the binary at /usr/bin/wkhtmltopdf.  
# Ubuntu repository package places it correctly, but the .deb package  
# from the project page does not.  
RUN \  
curl --fail --location --output wkhtmltox.deb \  
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.2.1/wkhtmltox-0.12.2.1_linux-
trusty-amd64.deb && \  
dpkg -i wkhtmltox.deb && \  
rm -v wkhtmltox.deb && \  
ln -s /usr/local/bin/wkhtmltopdf /usr/bin/wkhtmltopdf  
#############################################################################  
  
#############################################################################  
### db-clients  
#############################################################################  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y \  
mongodb-clients \  
mysql-client \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
#############################################################################  
  
#############################################################################  
### PhpUnit  
#############################################################################  
RUN \  
curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
composer global --verbose require "phpunit/phpunit-selenium=1.x" && \  
composer clear-cache --verbose && \  
ln -vs /root/.composer/vendor/bin/phpunit /usr/bin/phpunit  
#############################################################################  
  
RUN \  
pip install hchk  
  
RUN \  
mkdir -vp /cloe && \  
mkdir -vp /etc/cloe_run/first-run.d && \  
mkdir -vp /etc/cloe_run/pre-run.d && \  
mkdir -vp /etc/cloe_run/post-run.d && \  
mkdir -vp /etc/cloe_run/last-run.d  
  
ADD files/cloe_run /etc/default/cloe_run  
ADD files/usr/local/bin/cloe_run /usr/local/bin/  
ADD files/hchk /etc/cloe_run/post-run.d/  
  
RUN \  
chmod -v a+x \  
/usr/local/bin/cloe_run \  
/etc/cloe_run/post-run.d/hchk  
  
ADD ./etc/msmtprc /etc/msmtprc  
  
ENTRYPOINT [ "cloe_run", "${CLOE_RUN_BIN}" ]  

