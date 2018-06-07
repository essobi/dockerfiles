FROM debian  
  
RUN apt-get update \  
&& apt-get -qy upgrade \  
&& DEBIAN_FRONTEND=noninteractive apt-get -qy install \  
apache2 \  
graphite-carbon \  
graphite-web \  
libapache2-mod-wsgi \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN cp /usr/share/graphite-web/apache2-graphite.conf /etc/apache2/sites-
available/graphite.conf \  
&& a2ensite graphite \  
&& a2dissite 000-default  
  
# Current docker version of Ubuntu xenial does not allow input onto rootfs, so
two ADDs have to be used.  
ADD run.sh /srv/run.sh  
ADD default-graphite-carbon /etc/default/graphite-carbon  
  
CMD /srv/run.sh  

