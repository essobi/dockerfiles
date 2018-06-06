FROM samos123/drupal  
MAINTAINER Nasser Alansari <alansari.n@nyu.edu>  
  
# Install packages  
RUN apt-get -q update && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq --no-install-recommends install \  
wget patch git \  
cron \  
logrotate  
  
# Add logrotate conf  
ADD logrotate.d/tripal /etc/logrotate.d/  
  
# Compile a php7 compatible version of uploadprogress modules  
WORKDIR /tmp  
RUN git clone https://github.com/php/pecl-php-uploadprogress.git \  
&& cd pecl-php-uploadprogress && phpize \  
&& ./configure \  
&& make \  
&& make install  
  
#==== Tripal installation ====================================================  
WORKDIR /var/www/html/sites/all/modules  
ENV TRIPAL_VERSION="tripal-7.x-2.x-"  
ENV CHADO_INSTALL_OPTION="Install Chado v1.3"  
# Download modules  
RUN drush pm-download ctools views ${TRIPAL_VERSION}  
  
# Applying patch: A bug exists in Drupal related to the bytea data type in
PostgreSQL  
WORKDIR /var/www/html  
RUN wget --no-check-certificate https://drupal.org/files/drupal.pgsql-
bytea.27.patch && patch -p1 < drupal.pgsql-bytea.27.patch  
  
# Applying patch: a bug in the Drupal Views 3.0 code that prevents Tripal's
administrative and search data views from functioning  
WORKDIR /var/www/html/sites/all/modules/views  
RUN patch -p1 < ../tripal/tripal_views/views-sql-compliant-three-tier-
naming-1971160-22.patch  
  
ADD scripts/ /scripts  
  
ENV TRIPAL_GIT_CLONE_MODULES=""  
ENV TRIPAL_DOWNLOAD_MODULES=""  
ENV TRIPAL_ENABLE_MODULES="tripal_genetic tripal_natural_diversity
tripal_phenotype tripal_project tripal_pub tripal_stock"  
# Add PHP-settings  
ADD php-conf.d/ $PHP_INI_DIR/conf.d/  
  
# SSH  
RUN apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
RUN echo 'root:changeme' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
EXPOSE 22  

