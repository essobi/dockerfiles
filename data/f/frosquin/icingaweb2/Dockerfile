# Icinga2 Docker file  
FROM ubuntu:14.04  
MAINTAINER Frank Rosquin <frank.rosquin@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV APT_OPTIONS "-y --no-install-recommends --no-install-suggests -q"  
# ca-certificates icingaweb2  
RUN apt-get update \  
&& apt-get $APT_OPTIONS install wget \  
&& wget -O - http://packages.icinga.org/icinga.key | apt-key add - \  
&& echo "deb http://packages.icinga.org/ubuntu icinga-trusty main" >
/etc/apt/sources.list.d/icinga.list \  
&& echo "deb-src http://packages.icinga.org/ubuntu icinga-trusty main" >>
/etc/apt/sources.list.d/icinga.list \  
&& apt-get update  
  
RUN apt-get $APT_OPTIONS install \  
php5 php5-ldap php5-pgsql php5-mysqlnd \  
apache2 \  
icingaweb2 icingaweb2-module-monitoring \  
&& apt-get purge -y -q --auto-remove gcc make wget  
  
#RUN /usr/bin/icingacli setup config webserver apache > /etc/apache2/sites-
available/icingaweb2.conf  
ADD icinga2.conf /etc/apache2/sites-available/icingaweb2.conf  
RUN a2ensite icingaweb2  
RUN a2dissite 000-default  
ADD icingaweb2.sh /icingaweb2.sh  
RUN chmod 755 /icingaweb2.sh  
  
ADD inifiles/*.ini /etc/icingaweb2/  
ADD inifiles/modules/monitoring/*.ini /etc/icingaweb2/modules/monitoring/  
RUN mkdir /etc/icingaweb2/enabledModules  
RUN ln -s /usr/share/icingaweb2/modules/monitoring
/etc/icingaweb2/enabledModules/monitoring  
  
ENTRYPOINT ["/icingaweb2.sh"]  

