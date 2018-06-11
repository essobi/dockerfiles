FROM yieldr/debian  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends apache2 \  
&& apt-get clean  
  
RUN set -x \  
&& a2enmod rewrite \  
&& a2enmod remoteip \  
&& ln -sf /dev/stdout /var/log/apache2/access.log \  
&& ln -sf /dev/stderr /var/log/apache2/error.log  
  
EXPOSE 80  
  
CMD ["apachectl", "-D", "FOREGROUND"]  

