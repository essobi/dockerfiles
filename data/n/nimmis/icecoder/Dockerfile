FROM nimmis/apache-php5  
  
MAINTAINER nimmis <kjell.havneskold@gmail.com>  
  
# disable interactive functions  
ENV DEBIAN_FRONTEND noninteractive  
  
  
RUN wget https://icecoder.net/download-zip?version=5.0 -O /icecoder.zip && \  
unzip -q /icecoder.zip -d /root/ && \  
mv /root/ICE* /var/www/html/icecoder && \  
chown -R www-data.www-data /var/www/html/icecoder && \  
rm -f /icecoder.zip  

