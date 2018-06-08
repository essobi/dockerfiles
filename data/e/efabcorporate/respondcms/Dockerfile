##############################################################  
# Crée un container docker pour le CMS RespondCMS  
##############################################################  
  
FROM tutum/apache-php  
MAINTAINER Fredice NJAKO "fredice.njako@efab-corporate.com"  
LABEL version="1.0.1"  
LABEL description="Respond CMS"  
  
  
##########################################################  
# Installation des librairies necéssaires  
##########################################################  
RUN \  
apt-get -qq update && \  
apt-get -qq install git mysql-client && \  
apt-get clean  
##########################################################  
  
ENV RESPOND_HOME "/var/www/html"  
  
##########################################################  
# Récupération des sources  
##########################################################  
RUN mkdir -p $RESPOND_HOME; rm -R $RESPOND_HOME;  
RUN git clone https://github.com/madoublet/respond.git $RESPOND_HOME  
RUN mkdir -p $RESPOND_HOME/sites  
##########################################################  
  
##########################################################  
# Copie des scripts de configuration  
##########################################################  
COPY entrypoint.sh /entrypoint.sh  
COPY ./conf/default.conf /etc/apache2/sites-available/000-default.conf  
##########################################################  
  
##########################################################  
# Positionnement des droits  
##########################################################  
RUN chown -R www-data:www-data $RESPOND_HOME  
RUN chmod -R 755 $RESPOND_HOME  
##########################################################  
  
##########################################################  
# Installation du module rewrite  
##########################################################  
RUN sudo a2enmod rewrite  
##########################################################  
  
##########################################################  
# Lancement du contenair  
##########################################################  
EXPOSE 80 443  
WORKDIR $RESPOND_HOME  
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  
##########################################################

