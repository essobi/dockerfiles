FROM debian:sid  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -qy install \  
apache2 \  
graphite-carbon \  
graphite-web \  
libapache2-mod-wsgi \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD content/ /  
  
RUN cp /usr/share/graphite-web/apache2-graphite.conf /etc/apache2/sites-
available/graphite.conf \  
&& a2ensite graphite \  
&& a2dissite 000-default  
  
CMD /srv/run.sh  

