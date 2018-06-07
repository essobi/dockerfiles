FROM enoniccloud/apache2  
  
MAINTAINER Erik Kaareng-Sunde <esu@enonic.com>  
  
RUN rm /etc/apache2/sites-enabled/000-default.conf  
RUN rm /etc/apache2/sites-enabled/default-ssl.conf  
  
RUN apt-get update && apt-get -y install curl && apt-get clean  
RUN curl -o /usr/local/bin/certbot-auto https://dl.eff.org/certbot-auto && \  
chmod +x /usr/local/bin/certbot-auto && \  
certbot-auto --os-packages-only -n  
  
COPY index.html /var/www/html/index.html  
COPY launcher.sh /usr/local/bin/launcher.sh  
RUN chmod +x /usr/local/bin/launcher.sh  
  
CMD /usr/local/bin/launcher.sh  

