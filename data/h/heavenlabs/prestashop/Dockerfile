FROM heavenlabs/prestashop_base:7.0-apache  
LABEL maintainer="Jakub Stejskal <jstejskal@mojemana.cz>"  
  
ENV PS_VERSION 1.7.3.2  
# Get PrestaShop  
ADD https://www.prestashop.com/download/old/prestashop_1.7.3.2.zip
/tmp/prestashop.zip  
  
# Extract  
RUN mkdir -p /tmp/data-ps \  
&& unzip -q /tmp/prestashop.zip -d /tmp/data-ps/ \  
&& bash /tmp/ps-extractor.sh /tmp/data-ps \  
&& rm /tmp/prestashop.zip  

