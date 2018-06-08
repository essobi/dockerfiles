FROM meanbee/magento:5.6-cli  
  
MAINTAINER Nick Jones <nick.jones@meanbee.com>  
  
RUN apt-get update && apt-get install -y mysql-client  
  
# Download the latest version of magerun  
RUN curl http://files.magerun.net/n98-magerun-latest.phar -o /n98-magerun.phar  
RUN chmod +x /n98-magerun.phar  
  
# Add our magerun wrapper  
COPY magerun-wrapper.sh /magerun-wrapper.sh  
RUN chmod +x /magerun-wrapper.sh  
  
# Allow for magerun commands to specified  
ENTRYPOINT [ "/magerun-wrapper.sh" ]  

