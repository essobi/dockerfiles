FROM ubuntu:16.04  
MAINTAINER Jonas Renggli <jonas.renggli@visol.ch>  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update \  
&& apt-get install -y \  
php-apcu \  
php-common \  
php-imagick \  
php-redis \  
php7.0-cli \  
php7.0-common \  
php7.0-curl \  
php7.0-gd \  
php7.0-intl \  
php7.0-json \  
php7.0-mbstring \  
php7.0-mcrypt \  
php7.0-mysql \  
php7.0-opcache \  
php7.0-readline \  
php7.0-soap \  
php7.0-xml \  
php7.0-zip \  
&& apt-get purge -y php-igbinary \  
&& rm -r /var/lib/apt/lists/*  
  
RUN apt-get update \  
&& apt-get install -y \  
apache2 \  
apache2-bin \  
apache2-data \  
apache2-utils \  
libapache2-mod-php7.0 \  
&& rm -r /var/lib/apt/lists/*  
  
RUN apt-get update \  
&& apt-get install -y \  
python \  
python-apport \  
python-apt \  
python-apt-common \  
python-attr \  
python-cffi-backend \  
python-configobj \  
python-crypto \  
python-cryptography \  
python-dbus \  
python-dbus-dev \  
python-enum34 \  
python-gdbm \  
python-gi \  
python-gnupg \  
python-httplib2 \  
python-idna \  
python-ipaddress \  
python-keyring \  
python-launchpadlib \  
python-lazr.restfulclient \  
python-lazr.uri \  
python-ldb \  
python-minimal \  
python-newt \  
python-oauth \  
python-openssl \  
python-pam \  
python-pkg-resources \  
python-problem-report \  
python-pyasn1 \  
python-pyasn1-modules \  
python-samba \  
python-secretstorage \  
python-serial \  
python-service-identity \  
python-simplejson \  
python-six \  
python-talloc \  
python-tdb \  
python-twisted-bin \  
python-twisted-core \  
python-wadllib \  
python-zope.interface \  
python2.7 \  
python2.7-minimal \  
python3 \  
python3-apport \  
python3-apt \  
python3-chardet \  
python3-dbus \  
python3-debian \  
python3-distupgrade \  
python3-gdbm:amd64 \  
python3-gi \  
python3-minimal \  
python3-pkg-resources \  
python3-problem-report \  
python3-requests \  
python3-six \  
python3-systemd \  
python3-update-manager \  
python3-urllib3 \  
python3.5 \  
python3.5-minimal \  
&& rm -r /var/lib/apt/lists/*  
  
RUN apt-get update \  
&& apt-get install -y \  
rake \  
ruby \  
ruby-augeas \  
ruby-deep-merge \  
ruby-did-you-mean \  
ruby-json \  
ruby-minitest \  
ruby-net-telnet \  
ruby-nokogiri \  
ruby-power-assert \  
ruby-rgen \  
ruby-safe-yaml \  
ruby-selinux \  
ruby-shadow \  
ruby-test-unit \  
ruby2.3 \  
ruby2.3-dev:amd64 \  
rubygems-integration \  
&& rm -r /var/lib/apt/lists/*  
  
RUN apt-get update \  
&& apt-get install -y \  
openjdk-8-jre:amd64 \  
openjdk-8-jre-headless:amd64 \  
&& rm -r /var/lib/apt/lists/*  
  
RUN apt-get update \  
&& apt-get install -y \  
perl \  
perl-modules-5.22 \  
&& rm -r /var/lib/apt/lists/*  
  
#RUN apt-get update \  
# && apt-get install -y \  
# ubuntu-standard \  
# && rm -r /var/lib/apt/lists/*  
  
RUN apt-get update \  
&& apt-get install -y \  
aptitude \  
aptitude-common \  
apt-transport-https \  
apt-utils \  
at \  
augeas-lenses \  
awstats \  
bash-completion \  
bc \  
binutils \  
build-essential \  
busybox-initramfs \  
busybox-static \  
bzip2 \  
ca-certificates \  
ca-certificates-java \  
catdoc \  
command-not-found \  
cron \  
curl \  
dnsutils \  
exiftags \  
facter \  
fakeroot \  
file \  
ftp \  
fuse \  
geoip-database-contrib \  
gettext-base \  
ghostscript \  
git \  
git-core \  
git-man \  
graphicsmagick \  
gsfonts \  
gsfonts-x11 \  
hiera \  
htmldoc \  
htmldoc-common \  
htop \  
ifupdown \  
imagemagick \  
imagemagick-6.q16 \  
imagemagick-common \  
info \  
iotop \  
iproute \  
iproute2 \  
iptables \  
iptables-persistent \  
iputils-ping \  
iputils-tracepath \  
iso-codes \  
java-common \  
javascript-common \  
kbd \  
keyboard-configuration \  
keyutils \  
klibc-utils \  
less \  
locales \  
logrotate \  
logtail \  
lsb-release \  
lshw \  
lsof \  
ltrace \  
lvm2 \  
man-db \  
manpages \  
manpages-dev \  
mc \  
mc-data \  
memtest86+ \  
mime-support \  
mlocate \  
mysql-client \  
mysql-client-5.7 \  
mysql-client-core-5.7 \  
mysql-common \  
nano \  
netbase \  
netcat \  
netcat-openbsd \  
netcat-traditional \  
netfilter-persistent \  
netpbm \  
net-tools \  
nfs-common \  
ntp \  
ntpdate \  
openssh-client \  
openssh-server \  
openssh-sftp-server \  
openssl \  
parted \  
passwd \  
pastebinit \  
patch \  
pciutils \  
plymouth \  
plymouth-theme-ubuntu-text \  
policykit-1 \  
poppler-data \  
poppler-utils \  
popularity-contest \  
postfix \  
powermgmt-base \  
procps \  
psmisc \  
puppet \  
puppet-common \  
pwgen \  
rake \  
rename \  
rpcbind \  
rsync \  
rsyslog \  
rsyslog-gnutls \  
rsyslog-relp \  
run-one \  
samba-common \  
samba-common-bin \  
samba-libs:amd64 \  
screen \  
sgml-base \  
shared-mime-info \  
smbclient \  
snmp \  
sound-theme-freedesktop \  
ssh-import-id \  
ssl-cert \  
strace \  
subversion \  
sudo \  
tcpd \  
tcpdump \  
telnet \  
time \  
tmux \  
ttf-dejavu-core \  
tzdata \  
ucf \  
unrtf \  
unzip \  
vim \  
vim-common \  
vim-runtime \  
vim-tiny \  
wget \  
whois \  
xml-core \  
xpdf \  
xz-utils \  
zip \  
zsh \  
zsh-common \  
&& rm -r /var/lib/apt/lists/*  
  
RUN apt-get update \  
&& apt-get install -y \  
supervisor \  
&& rm -r /var/lib/apt/lists/*  
  
RUN mkdir /var/run/sshd && chmod 0755 /var/run/sshd  
  
COPY assets/ /  
  
RUN a2enmod \  
authz_groupfile \  
cgi \  
expires \  
headers \  
remoteip \  
rewrite \  
socache_shmcb \  
ssl  
  
RUN rm /etc/apache2/sites-enabled/000-default.conf  
  
RUN usermod -d /home/www-data www-data \  
&& chsh www-data -s /bin/bash  
  
RUN mkdir -p /home/www-data/default/releases/current/web \  
&& mkdir -p /home/www-data/logs/ \  
&& chown -R www-data:www-data /home/www-data  
  
WORKDIR /home/www-data/default/releases/current  
  
EXPOSE 80 22  
  
CMD /usr/bin/supervisord -n -c /etc/supervisor/supervisord.conf  

