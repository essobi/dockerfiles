FROM ubuntu:16.04  
LABEL author_name="Bigfathom"  
LABEL author_website="https://bigfathom.org"  
LABEL environment_context="DEV"  
  
ADD ./machine-scripts /var/machine-scripts  
  
#Install core utilities  
ARG APT_GET_FORCED_DATE=2018-04-14  
RUN apt-get update  
RUN apt-get install -y apt-utils  
  
#INSTALL APACHE2  
RUN apt-get install -y apache2  
RUN a2enmod rewrite  
  
# INSTALLING PHP  
RUN apt-get install -y php7.0  
RUN apt-get install -y php7.0-gmp  
RUN apt-get install -y php7.0-curl  
RUN apt-get install -y php7.0-gd  
RUN apt-get install -y php7.0-mbstring  
RUN apt-get install -y php7.0-json  
RUN apt-get install -y php7.0-xml  
RUN apt-get install -y php7.0-mysql  
RUN apt-get install -y php7.0-opcache  
RUN apt-get install -y php7.0-gmp  
RUN apt-get install -y libapache2-mod-php7.0  
RUN apt-get install -y php7.0-cli  
  
#Install some critical utilities now  
RUN apt-get install -y curl  
RUN apt-get install -y git  
RUN apt-get install -y rsync  
  
#Install DRUPAL7 to docroot  
# See https://www.drupal.org/node/3060/release  
WORKDIR /var/www/html  
RUN rm -rf /var/www/html  
#ARG DRUPAL_VERSION=7.58  
#ARG DRUPAL_MD5=c59949bcfd0d68b4f272bc05a91d4dc6  
#RUN curl -fSL
"https://ftp.drupal.org/files/projects/drupal-${DRUPAL_VERSION}.tar.gz" -o
drupal.tar.gz \  
# && echo "${DRUPAL_MD5} *drupal.tar.gz" | md5sum -c - \  
# && tar -xz --strip-components=1 -f drupal.tar.gz \  
# && rm drupal.tar.gz  
ARG DRUPAL_VERSION=7.58  
RUN curl -fSL
"https://ftp.drupal.org/files/projects/drupal-${DRUPAL_VERSION}.tar.gz" -o
drupal.tar.gz \  
&& tar -xz --strip-components=1 -f drupal.tar.gz \  
&& rm drupal.tar.gz  
  
#Install drush  
RUN apt-get update  
RUN apt-get install -y drush  
  
#Install the Bigfathom application content  
ADD bigfathom-bucket /var/local/bigfathom-bucket  
WORKDIR /var/local/bigfathom-bucket  
RUN git clone https://github.com/bigfathom/bigfathom_application.git  
WORKDIR /var/local/bigfathom-bucket  
RUN ls -la && echo "Placing Bigfathom application files on webserver ..."  
RUN rsync -vrah ./bigfathom_application/drupal7/default /var/www/html/sites  
RUN rsync -vrah ./bigfathom_application/drupal7/all/libraries
/var/www/html/sites/all  
RUN rsync -vrah ./bigfathom_application/drupal7/all/modules/additional
/var/www/html/sites/all/modules  
#RUN rsync -vrah ./bigfathom_application/drupal7/all/themes
/var/www/html/sites/all  
#Link the Bigfathom contents to the repo rather than just copy to the website  
WORKDIR /var/www/html/sites/all/modules  
RUN ln -s /var/local/bigfathom-
bucket/bigfathom_application/drupal7/all/modules/just_bigfathom just_bigfathom  
WORKDIR /var/www/html/sites/all/themes  
RUN ln -s /var/local/bigfathom-
bucket/bigfathom_application/drupal7/all/themes/omega omega  
RUN ln -s /var/local/bigfathom-
bucket/bigfathom_application/drupal7/all/themes/omega_bigfathom
omega_bigfathom  
  
#Set the ownership of all the files  
WORKDIR /var/www/html  
RUN chgrp -R www-data .  
RUN chown -R www-data:www-data sites  
  
#Prep the environment for final configuration steps and DEV use of the box  
WORKDIR /var/local/bigfathom-bucket  
RUN echo "Remove this file after initializing bigfathom setup once" >
"NOT_INITIALIZED_YET.flag"  
RUN echo "ENVIRONMENT=DEV" > docker-build.txt  
RUN curl -4 --connect-timeout 10 https://bigfathom.org/docker-build >> docker-
build.txt || echo "\nNo https://bigfathom.org/docker-build update info
available\n"  
RUN apt-get install -y ufw  
RUN echo "Installed ufw" >> docker-build.txt  
RUN apt-get install -y less vim  
RUN echo "Installed less vim" >> docker-build.txt  
RUN apt-get install -y mysql-client-core-5.7  
RUN echo "Installed mysql client" >> docker-build.txt  
RUN echo "MACHINE_BUILD_FINISHED_TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
>> docker-build.txt  
  
ENV DOCKERFILE_MACHINEBUILD_VERSION "20180414.beta.1"  
#Finish at a good folder for DEVs at login  
WORKDIR /var/www/html  
  
#Invoke the startup script  
CMD /var/machine-scripts/custom/starup.sh INIT  
  

