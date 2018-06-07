FROM harnesscloud/conpaas-director-base  
MAINTAINER Mark Stillwell <mark@stillwell.me>  
  
# prepare working directory  
RUN mkdir -p /var/cache/docker/workdirs && \  
git clone -b harness https://github.com/ConPaaS-team/conpaas.git \  
/var/cache/docker/workdirs/conpaas  
WORKDIR /var/cache/docker/workdirs/conpaas  
  
# install conpaas  
#RUN git checkout 663ee61f644474684bca61497ed8b9a7888f11c6  
RUN bash mkdist.sh 1.5.0 && \  
tar -xaf cpsdirector-*.tar.gz && \  
tar -xaf cpsfrontend-*.tar.gz && \  
easy_install --always-unzip cpslib-*.tar.gz && \  
easy_install --always-unzip cpsclient-*.tar.gz && \  
rm -rf *.tar.gz && \  
cp -r cpsfrontend-*/www/* /var/www && \  
rm /var/www/index.html && \  
cp /var/www/config-example.php /var/www/config.php && \  
a2enmod ssl && \  
a2ensite default-ssl && \  
cd cpsdirector-* && \  
echo 0.0.0.0 | make install && \  
cd .. && \  
cp cpsfrontend-*/conf/main.ini /etc/cpsdirector/main.ini && \  
cp cpsfrontend-*/conf/welcome.txt /etc/cpsdirector/welcome.txt && \  
chown www-data:www-data /var/log/apache2 && \  
a2ensite conpaas-director  
  
# create startup scripts  
ADD conpaas-director.sh /etc/my_init.d/10-conpaas-director  
ADD php.ini /etc/php5/apache2/  
RUN chmod 0755 /etc/my_init.d/10-conpaas-director  
  
# data volumes  
VOLUME [ "/etc/apache2", "/etc/cpsdirector", "/var/log/apache2" ]  
  
# interface ports  
EXPOSE 22 80 443 5555  

