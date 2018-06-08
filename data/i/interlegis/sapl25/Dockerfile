FROM ubuntu:12.04  
MAINTAINER "Fabio Rauber" <fabiorauber@gmail.com>  
  
ENV SVNSOURCE="http://repositorio.interlegis.gov.br/ILSAPL/install/2.5/" \  
INSTALLSRC="/usr/local/src/sapl25" \  
INSTALLDIR="/opt/interlegis/SAPL25" \  
LANG="pt_BR.UTF-8" \  
LANGUAGE="pt_BR:pt" \  
LC_ALL="pt_BR.UTF-8" \  
ADMINPW="admin" \  
MYSQL_PASSWORD="mysqlInterlegis" \  
MYSQL_HOST="mysql" \  
MYSQL_DATABASE="sapl" \  
MYSQL_USER="sapl" \  
ZEO_CLIENT=false \  
ZEO_ADDRESS="zeoserver:8100" \  
SAPL_EMAIL="sapl@localhost" \  
SAPL_SMTP_HOST="localhost" \  
SAPL_SMTP_PORT="25" \  
SAPL_PASSWORD="altereme" \  
SAPL_NAME="Municipio - UF" \  
SAPL_HOSTNAME="localhost" \  
SAPL_PROTOCOL="http"  
  
RUN apt-get update && apt-get -y upgrade && \  
apt-get install -y \  
language-pack-pt-base \  
build-essential \  
zlib1g-dev \  
libjpeg62-dev \  
libssl-dev \  
openssl \  
libreadline6-dev \  
libreadline6 \  
readline-common \  
libxml2-dev \  
wv \  
poppler-utils \  
libxslt1-dev \  
libfreetype6-dev \  
xpdf-utils \  
gs-common \  
catdoc \  
ppthtml \  
subversion \  
unzip \  
lynx \  
mysql-client \  
libmysqlclient-dev \  
mailutils \  
subversion && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY src/start.sh /usr/bin/start  
  
RUN mkdir -p $INSTALLSRC && \  
groupadd -g 501 zope && \  
useradd -g 501 -u 501 -m -s /bin/bash zope && \  
chmod +x /usr/bin/start && \  
locale-gen pt_BR.UTF-8  
  
WORKDIR $INSTALLSRC  
  
RUN /usr/bin/svn co $SVNSOURCE install_sapl  
COPY src/install.sh $INSTALLSRC/install_sapl  
COPY src/setup_py.patch $INSTALLSRC  
  
RUN cd install_sapl && \  
/bin/bash install.sh && \  
rm -rf $INSTALLSRC/install_sapl && \  
touch $INSTALLDIR/instances/sapl25/log/event.log && \  
chown -R zope:zope $INSTALLDIR/instances/sapl25 && \  
cp $INSTALLDIR/instances/sapl25/Products/ILSAPL/import/*
$INSTALLDIR/instances/sapl25/import/  
  
COPY src/sapl_create.py $INSTALLDIR/sapl_create.py  
  
ADD src/FSDump.tar.gz $INSTALLDIR/instances/sapl25/Products  
  
RUN chown -R zope:zope $INSTALLDIR/instances/sapl25/Products/FSDump  
  
WORKDIR $INSTALLDIR  
USER zope  
  
EXPOSE 8080  
  
CMD ["start"]  

