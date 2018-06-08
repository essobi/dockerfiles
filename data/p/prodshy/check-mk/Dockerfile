FROM gliderlabs/alpine  
  
ENV NAGIOS_VERSION 4.1.0rc1  
ENV NAGIOS_PLUGINS_VERSION 2.0.3  
ENV PNP4NAGIOS_VERSION 0.6.24  
ENV CHECKMK_VERSION 1.2.5i6p4  
  
ENV NAGIOS_URL
http://downloads.sourceforge.net/project/nagios/nagios-4.x/nagios-4.1.0/nagios-$NAGIOS_VERSION.tar.gz  
ENV NAGIOSPLUGIN_URL http://nagios-plugins.org/download/nagios-
plugins-$NAGIOS_PLUGINS_VERSION.tar.gz  
ENV PNP4NAGIOS_URL
http://downloads.sourceforge.net/project/pnp4nagios/PNP-0.6/pnp4nagios-$PNP4NAGIOS_VERSION.tar.gz  
ENV CHECKMK_URL http://mathias-
kettner.com/download/check_mk-$CHECKMK_VERSION.tar.gz  
  
RUN apk-install bash sudo curl perl php python apache2 php-apache2 php-iconv
rrdtool gd-dev libpng-dev jpeg-dev supervisor  
  
RUN addgroup nagios  
RUN adduser -G nagios -g "Nagios" -s /bin/bash -D nagios  
RUN adduser apache nagios  
  
RUN apk-install g++ make && \  
curl -L -k $NAGIOS_URL | gzip -d |tar -xf - && \  
cd nagios-$NAGIOS_VERSION && \  
./configure && \  
make all && \  
make install && \  
make install-config && \  
make install-commandmode && \  
make install-webconf && \  
apk del g++ make && \  
rm -fr /nagios-$NAGIOS_VERSION  
RUN echo "nagiosadmin:M.t9dyxR3OZ3E" > /usr/local/nagios/etc/htpasswd.users  
RUN chown nagios:nagios /usr/local/nagios/etc/htpasswd.users  
  
RUN apk-install g++ make && \  
curl -L -k $NAGIOSPLUGIN_URL | gzip -d |tar -xf - && \  
cd nagios-plugins-$NAGIOS_PLUGINS_VERSION && \  
./configure && \  
make && \  
make install && \  
apk del g++ make && \  
rm -fr /nagios-plugins-$NAGIOS_PLUGINS_VERSION  
  
RUN apk-install g++ make && \  
curl -L -k $PNP4NAGIOS_URL | gzip -d |tar -xf - && \  
cd pnp4nagios-$PNP4NAGIOS_VERSION && \  
./configure --with-perfdata-dir=/data/perfdata --with-perfdata-spool-
dir=/data/perfspool && \  
make all && \  
make fullinstall && \  
apk del g++ make && \  
rm -fr /pnp4nagios-$PNP4NAGIOS_VERSION /usr/local/pnp4nagios/share/install.php
/usr/local/pnp4nagios/etc/config_local.php  
COPY pnp4nagios/ /usr/local/pnp4nagios/etc/  
  
COPY check_mk/check_mk_setup.conf /root/.check_mk_setup.conf  
RUN sed "s/NAGIOS_VERSION/$NAGIOS_VERSION/g" -i /root/.check_mk_setup.conf  
RUN apk-install g++ make && \  
curl -L -k $CHECKMK_URL | gzip -d |tar -xf - && \  
cd check_mk-$CHECKMK_VERSION && \  
./setup.sh --yes && \  
apk del g++ make && \  
rm -fr /check_mk-$CHECKMK_VERSION /root/.check_mk_setup.conf  
  
RUN apk-install g++ make flex apache2-dev python-dev && \  
curl -L -k http://dist.modpython.org/dist/mod_python-3.5.0.tgz | gzip -d |tar
-xf - && \  
cd mod_python-3.5.0 && \  
sed -i -e '/^GIT/d' -e 's/-$GIT//' dist/version.sh && \  
./configure --with-apxs=/usr/bin/apxs && \  
make && \  
make install_dso install_py_lib && \  
apk del g++ make flex apache2-dev python-dev && \  
rm -fr /mod_python-3.5.0  
COPY check_mk/mod_python /etc/apache2/conf.d/mod_python.load  
RUN echo "Include /etc/apache2/conf.d/*.load" >> /etc/apache2/httpd.conf  
RUN sed -e '1s/^.*/LoadModule python_module modules\/mod_python.so/' -e
'/^#/d' -i /etc/apache2/conf.d/zzz_check_mk.conf  
  
RUN apk-install g++ python-dev py-pip && \  
pip install nagios-plugin-elasticsearch && \  
apk del g++ python-dev py-pip  
  
COPY nagios/nagios.cfg /usr/local/nagios/etc/  
COPY nagios/commands.cfg /usr/local/nagios/etc/objects/  
COPY nagios/nagios.init /etc/init.d/nagios  
COPY supervisord.conf /etc/supervisord.conf  
RUN chmod 755 /etc/init.d/nagios  
RUN mkdir /var/run/rrdcached /data/rrdcached.journal /data/nagios.perfdump  
RUN chown nagios.nagios -R /usr/local/nagios/var/rw /data /var/run/rrdcached
/usr/local/pnp4nagios/etc  
RUN chmod g+s /usr/local/nagios/var/rw  
RUN chmod g+w -R /var/lib/mkeventd /etc/check_mk /var/lib/check_mk  
  
VOLUME /data  
VOLUME /usr/local/nagios/var  
  
ADD /bin/start /bin/start  
ENTRYPOINT [ "/bin/bash" ]  
CMD [ "/bin/start" ]  
  
EXPOSE 80  

