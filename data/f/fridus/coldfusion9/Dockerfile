FROM msealand/cf9  
MAINTAINER fridus  
  
env TZ Europe/Brussels  
  
# gateway  
ADD ./build/cfapi/Gateway.cfc /var/www/CF/Gateway.cfc  
  
# apache modules  
RUN a2enmod rewrite && a2enmod headers  
  
# Timezone  
RUN echo $TZ | sudo tee /etc/timezone && sudo dpkg-reconfigure --frontend
noninteractive tzdata  
  
# Fix paths of assets  
RUN echo "Alias \"/CFIDE\" \"/opt/coldfusion9/wwwroot/CFIDE\"" >>
/etc/apache2/httpd.conf  
  
ADD ./build/start.sh /start.sh  
RUN chmod +x /start.sh  
  
CMD /start.sh  

