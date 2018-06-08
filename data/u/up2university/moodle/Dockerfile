FROM ubuntu:14.04  
MAINTAINER Sergio Gómez <sergio@quaip.com>  
  
# Keep upstart from complaining  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
#RUN echo "Acquire::http::proxy \"PROXY_ADDRESS/\";" > /etc/apt/apt.conf  
#RUN echo "Acquire::https::proxy \"PROXY_ADDRESS/\";" > /etc/apt/apt.conf  
RUN apt-get update  
RUN apt-get -y upgrade  
  
RUN apt-get -y install software-properties-common python-software-properties  
RUN apt-key adv --keyserver "hkp://keyserver.ubuntu.com:80" \--recv 'E5267A6C'  
  
RUN add-apt-repository ppa:ondrej/php  
RUN add-apt-repository ppa:certbot/certbot  
  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Basic Requirements  
#RUN apt-get -y install mysql-server mysql-client pwgen python-setuptools curl
git unzip  
RUN apt-get -y install python-setuptools unzip  
  
# Moodle Requirements  
RUN apt-get -y install apache2 php7.0 php7.0-gd libapache2-mod-php7.0 postfix
wget supervisor php7.0-pgsql vim curl libcurl3 libcurl3-dev php7.0-curl
php7.0-xml php7.0-xmlrpc php7.0-intl php7.0-mysql php7.0-zip php7.0-mbstring
php7.0-soap php7.0-mcrypt python-certbot-apache git  
  
RUN easy_install supervisor  
ADD ./start.sh /start.sh  
ADD ./foreground.sh /etc/apache2/foreground.sh  
ADD ./supervisord.conf /etc/supervisord.conf  
  
ADD ./000-default.conf /etc/apache2/sites-available/000-default.conf  
ADD ./default-ssl.conf /etc/apache2/sites-available/default-ssl.conf  
RUN ln -s /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-
enabled/rewrite.load  
RUN ln -s /etc/apache2/mods-available/ssl.load /etc/apache2/mods-
enabled/ssl.load  
RUN ln -s /etc/apache2/mods-available/ssl.conf /etc/apache2/mods-
enabled/ssl.conf  
RUN ln -s /etc/apache2/mods-available/socache_shmcb.load /etc/apache2/mods-
enabled/socache_shmcb.load  
RUN ln -s /etc/apache2/sites-available/default-ssl.conf /etc/apache2/sites-
enabled/default-ssl.conf  
  
ADD https://download.moodle.org/download.php/direct/stable33/moodle-
latest-33.tgz /var/www/moodle-latest.tgz  
RUN cd /var/www; rm -rf /var/www/html; tar zxvf moodle-latest.tgz; mv
/var/www/moodle /var/www/html  
RUN chown -R www-data:www-data /var/www/html/  
RUN mkdir /var/moodledata  
RUN chown -R www-data:www-data /var/moodledata; chmod 777 /var/moodledata  
RUN chmod 755 /start.sh /etc/apache2/foreground.sh  
  
ADD ./config-dist.php /var/www/html/config-dist.php  
  
ENV MYSQL_PASSWORD ${MYSQL_ROOT_PASSWORD}  
ENV MOODLE_PASSWORD ${MOODLE_PASSWORD}  
  
RUN echo "certbot --non-interactive --agree-tos --email \$CERT_EMAIL --apache
--domains \$VIRTUAL_HOST" > /certbot-setup.sh  
RUN chmod 755 /certbot-setup.sh  
  
RUN curl -L
https://moodle.org/plugins/download.php/14891/theme_fordson_moodle33_2017092500.zip
-o /fordson.zip  
RUN cp /fordson.zip /var/www/html/theme/  
RUN cd /var/www/html/theme; unzip fordson.zip  
  
RUN cd /var/www/html/auth; git clone https://github.com/catalyst/moodle-
auth_saml2.git saml2  
  
ADD ./pumoodle/filter.zip /var/www/html/filter/filter.zip  
RUN cd /var/www/html/filter/; unzip filter.zip  
  
ADD ./pumoodle/pmksearch.zip /var/www/html/repository/pmksearch.zip  
RUN cd /var/www/html/repository/; unzip pmksearch.zip  
  
ADD ./pumoodle/pumukit.zip /var/www/html/lib/editor/atto/plugins/pumukit.zip  
RUN cd /var/www/html/lib/editor/atto/plugins/; unzip pumukit.zip  
  
ADD ./pumoodle/pumukitpr.zip
/var/www/html/lib/editor/atto/plugins/pumukitpr.zip  
RUN cd /var/www/html/lib/editor/atto/plugins/; unzip pumukitpr.zip  
  
ADD ./pumoodle/filterpr.zip /var/www/html/filter/filterpr.zip  
RUN cd /var/www/html/filter/; unzip filterpr.zip  
  
ADD ./knockplop/knockplop.zip /var/www/html/mod/  
RUN cd /var/www/html/mod/; unzip knockplop.zip; rm knockplop.zip  
  
# Install H5P - mod/hvp version 1.6 from https://moodle.org/plugins/mod_hvp  
RUN curl -L
https://moodle.org/plugins/download.php/15518/mod_hvp_moodle34_2017112800.zip
-o /mod_hvp.zip  
RUN cp /mod_hvp.zip /var/www/html/mod/  
RUN cd /var/www/html/mod; unzip mod_hvp.zip  
  
# Install Plugin to use CERNBox as remote repository  
RUN git clone https://github.com/cernbox/moodle-repository_owncloud.git
/var/www/html/repository/owncloud  
RUN chown -R www-data:www-data /var/www/html/repository/owncloud  
  
# Install DSpace Sword plugin (push metadata to Dspace)  
RUN git clone -b up2u-develop
https://github.com/up2university/sword_upload.git
/var/www/html/repository/sword_upload  
RUN chown -R www-data:www-data /var/www/html/repository/sword_upload  
  
# Install DSpace API plugin (pull metadata from Dspace)  
RUN git clone -b up2u https://github.com/up2university/Moodle-Dspace-
Plugin.git /dspace  
RUN mv /dspace/dspace /var/www/html/repository/dspace  
RUN chown -R www-data:www-data /var/www/html/repository/dspace  
  
# Install logstore_xapi plugin to send learning records to LRS  
RUN curl -L https://github.com/xAPI-vle/moodle-
logstore_xapi/releases/download/v2.2.3/xapi.zip -o /xapi.zip \  
&& unzip /xapi.zip -d /var/www/html/admin/tool/log/store/ \  
&& rm /xapi.zip \  
&& chown -R www-data:www-data /var/www/html/admin/tool/log/store/xapi  
  
EXPOSE 80 443  
CMD ["/bin/bash", "/start.sh"]  

