##############################################################  
# Crée un container docker pour l'application Maarch Courrier  
##############################################################  
  
FROM java:openjdk-8-jre  
MAINTAINER Fredice NJAKO "fredice.njako@efab-corporate.com"  
  
ENV MAARCH_COURRIER_HOME /var/www/html/maarch_courrier  
ENV MAARCH_COURRIER_INSTALL_DIR /usr/src/maarch_courrier  
  
##########################################################  
# Installation des librairies necéssaires  
##########################################################  
RUN \  
apt-get -qq update && apt-get -qq upgrade && apt-get -qq dist-upgrade -y && \  
apt-get -qq install wget && \  
echo "deb http://packages.dotdeb.org jessie all" >
/etc/apt/sources.list.d/dotdeb.list && \  
wget -O- https://www.dotdeb.org/dotdeb.gpg | apt-key add - && \  
apt-get -qq update && \  
apt-get --purge -qq remove php5*  
  
RUN \  
apt-get -qq install \  
apache2 php7.0 php7.0-fpm libapache2-mod-php7.0 php7.0-cli php7.0-json
postgresql imagemagick wkhtmltopdf \  
php7.0-pgsql php7.0-gd subversion unzip p7zip p7zip-full php-pear xpdf-utils
php5-svn ghostscript \  
php7.0-xsl php7.0-xmlrpc php7.0-imap php7.0-imagick php7.0-soap
php7.0-mbstring \  
&& \  
apt-get clean  
  
RUN pear channel-discover pear.maarch.org  
RUN pear install maarch/CLITools-0.3.1  
##########################################################  
  
  
##########################################################  
# Récupération des sources maarch_courrier  
##########################################################  
RUN mkdir -p $MAARCH_COURRIER_HOME  
RUN mkdir -p $MAARCH_COURRIER_INSTALL_DIR  
RUN cd $MAARCH_COURRIER_INSTALL_DIR \  
&& svn checkout http://svn.maarch.org/core/branches/1.6
$MAARCH_COURRIER_INSTALL_DIR/ \  
&& svn checkout http://svn.maarch.org/maarch_entreprise/branches/1.6
$MAARCH_COURRIER_INSTALL_DIR/apps/maarch_entreprise \  
&& svn checkout http://svn.maarch.org/attachments/branches/1.6
$MAARCH_COURRIER_INSTALL_DIR/modules/attachments \  
&& svn checkout http://svn.maarch.org/avis/branches/1.6
$MAARCH_COURRIER_INSTALL_DIR/modules/avis \  
&& svn checkout http://svn.maarch.org/basket/branches/1.6
$MAARCH_COURRIER_INSTALL_DIR/modules/basket \  
&& svn checkout http://svn.maarch.org/cases/branches/1.6
$MAARCH_COURRIER_INSTALL_DIR/modules/cases \  
&& svn checkout http://svn.maarch.org/content_management/branches/1.6
$MAARCH_COURRIER_INSTALL_DIR/modules/content_management \  
&& svn checkout http://svn.maarch.org/entities/branches/1.6
$MAARCH_COURRIER_INSTALL_DIR/modules/entities \  
&& svn checkout http://svn.maarch.org/fileplan/branches/1.6
$MAARCH_COURRIER_INSTALL_DIR/modules/fileplan \  
&& svn checkout http://svn.maarch.org/folder/branches/1.6
$MAARCH_COURRIER_INSTALL_DIR/modules/folder \  
&& svn checkout http://svn.maarch.org/full_text/branches/1.6
$MAARCH_COURRIER_INSTALL_DIR/modules/full_text \  
&& svn checkout http://svn.maarch.org/ldap/branches/1.6
$MAARCH_COURRIER_INSTALL_DIR/modules/ldap \  
&& svn checkout http://svn.maarch.org/life_cycle/branches/1.6
$MAARCH_COURRIER_INSTALL_DIR/modules/life_cycle \  
&& svn checkout http://svn.maarch.org/notes/branches/1.6
$MAARCH_COURRIER_INSTALL_DIR/modules/notes \  
&& svn checkout http://svn.maarch.org/notifications/branches/1.6
$MAARCH_COURRIER_INSTALL_DIR/modules/notifications \  
&& svn checkout http://svn.maarch.org/reports/branches/1.6
$MAARCH_COURRIER_INSTALL_DIR/modules/reports \  
&& svn checkout http://svn.maarch.org/sendmail/branches/1.6
$MAARCH_COURRIER_INSTALL_DIR/modules/sendmail \  
&& svn checkout http://svn.maarch.org/tags/branches/1.6
$MAARCH_COURRIER_INSTALL_DIR/modules/tags \  
&& svn checkout http://svn.maarch.org/templates/branches/1.6
$MAARCH_COURRIER_INSTALL_DIR/modules/templates \  
&& svn checkout http://svn.maarch.org/thesaurus/branches/1.6
$MAARCH_COURRIER_INSTALL_DIR/modules/thesaurus \  
&& svn checkout http://svn.maarch.org/thumbnails/branches/1.6
$MAARCH_COURRIER_INSTALL_DIR/modules/thumbnails \  
&& svn checkout http://svn.maarch.org/visa/branches/1.6
$MAARCH_COURRIER_INSTALL_DIR/modules/visa  
##########################################################  
##########################################################  
# Configuration du niveau des logs  
##########################################################  
COPY conf/php.ini /etc/php7/apache2/php.ini  
COPY conf/default /etc/apache2/sites-available/default  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod 700 /entrypoint.sh  
RUN service php7.0-fpm restart  
RUN service apache2 restart  
##########################################################  
  
LABEL description="Maarch Courrier"  
LABEL version="1.6"  
  
##########################################################  
# Lancement du conteneur  
##########################################################  
EXPOSE 80 443  
WORKDIR $MAARCH_COURRIER_HOME  
VOLUME $MAARCH_COURRIER_HOME  
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  
##########################################################

