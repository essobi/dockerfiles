############################################################  
# Dockerfile to build Blast container image for the eBioKit  
# Based on wurmlab/sequenceserver  
# Version 0.9 September 2017  
# TODO:  
# - Auto add entries  
# - Sequenceserver logs  
# - Organize databases in folders? (genomic, protein...)  
############################################################  
  
# Set the base image to wurmlab/sequenceserver  
FROM ubuntu:16.04  
  
# File Author / Maintainer  
MAINTAINER Rafael Hernandez <https://github.com/fikipollo>  
  
################## BEGIN INSTALLATION ######################  
#Add the link to internal MRS service  
RUN apt-get update \  
&& apt-get -y install build-essential ruby ruby-dev ncbi-blast+ nginx php-fpm
apache2-utils sudo wget csh fcgiwrap \  
&& apt-get clean \  
&& gem install sequenceserver \  
&& gem install ncbi-blast-dbs  
  
RUN wget -O /tmp/wwwblast.tar.gz
https://github.com/fikipollo/wwwblast/archive/0.2.1.tar.gz  
  
ENV ADMIN_USER=admin \  
ADMIN_PASS=supersecret \  
MAX_FILE_SIZE=300 \  
CPU_NUMBER=4  
  
#Copy files  
COPY configs/* /tmp/  
  
RUN rm /var/www/html/* \  
&& mv /tmp/*.html /var/www/html/ \  
&& mv /tmp/*.png /var/www/html/ \  
&& mv /tmp/*.php /var/www/html/ \  
&& cat /tmp/rules >> /etc/sudoers \  
&& mv /tmp/default /etc/nginx/sites-available/ \  
&& mv /tmp/entrypoint.sh /usr/bin/entrypoint.sh \  
&& chmod +x /usr/bin/entrypoint.sh \  
&& mv /tmp/admin_tools /usr/local/bin/admin_tools \  
&& chmod +x /usr/local/bin/admin_tools \  
&& mv /tmp/sequenceserver /etc/init.d/sequenceserver \  
&& chmod +x /etc/init.d/sequenceserver \  
&& tar -xzvf /tmp/wwwblast.tar.gz -C /tmp/ \  
&& mv /tmp/wwwblast-* /var/www/html/blast \  
&& mv /var/www/html/blast/db /usr/local/src/original_db \  
&& ln -s /db /var/www/html/blast/db \  
&& rm -r /tmp/* \  
&& chown www-data:www-data /var/www/html/* \  
&& chmod 660 /var/www/html/*.* \  
&& htpasswd -b -c /etc/nginx/.htpasswd admin supersecret  
  
##################### INSTALLATION END #####################  
  
ENTRYPOINT ["/usr/bin/entrypoint.sh"]  

