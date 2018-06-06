FROM tutum/lamp  
MAINTAINER Chimera Entertainment GmbH  
  
# mysql and xibo user name is admin  
# data folder is /xibo-data/, also hardcoded in sql dump file which gets
imported  
ENV XIBO_VERSION 1.7.5  
ENV MYSQL_HOST localhost  
ENV MYSQL_PASS changeme  
ENV XIBO_ADMIN_PASS changeme  
ENV MYSQL_DBNAME xibo  
  
ADD run-xibo.sh /run-xibo.sh  
ADD create-mysql-xibo.sh /create-mysql-xibo.sh  
RUN chmod 755 /*.sh  
  
RUN apt-get update && apt-get install php5-gd php5-curl curl -y  
  
RUN curl -L https://github.com/docker-
infra/reefer/releases/download/v0.0.4/reefer.gz | \  
gunzip > /usr/bin/reefer && chmod a+x /usr/bin/reefer  
  
COPY templates /templates/  
  
RUN echo extension=mcrypt.so > /etc/php5/apache2/conf.d/20-mcrypt.ini  
  
RUN chmod o+w /app  
  
# switch to app home folder, symlink to /var/www/html  
WORKDIR /app  
  
# RUN curl https://github.com/xibosignage/xibo-
cms/archive/${XIBO_VERSION}.tar.gz -o xibo.tar.gz  
ADD https://github.com/xibosignage/xibo-cms/archive/${XIBO_VERSION}.tar.gz
xibo.tar.gz  
RUN tar -xvzf xibo.tar.gz --strip 1  
RUN rm -f xibo.tar.gz  
RUN rm -f install.php  
  
# create data dir for xibo  
RUN mkdir /xibo-data && chown www-data:www-data /xibo-data  
  
VOLUME /xibo-data/  
  
CMD [""]  
  
ENTRYPOINT [ "/usr/bin/reefer", \  
"-t", "/templates/settings.tmpl.php:/app/settings.php", \  
"-t", "/templates/xibo.tmpl.sql:/xibo.sql", \  
"-E", \  
"/run-xibo.sh" ]  

