from php:7.1-apache  
  
LABEL maintainer="daniel.secik@mzk.cz"  
  
RUN apt-get update && \  
apt-get install -y git && \  
rm -rf /var/lib/apt/lists/*  
  
COPY apache.conf /etc/apache2/sites-available/000-default.conf  
RUN ln -s /etc/apache2/mods-available/cgi.load /etc/apache2/mods-
enabled/cgi.load  
  
COPY scripts /scripts  
RUN chmod u+x /scripts/init.sh  
  
CMD [ "/scripts/init.sh" ]  

