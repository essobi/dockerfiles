FROM meanbee/magento:5.6-cli  
  
MAINTAINER Tom Robertshaw <tom.robertshaw@meanbee.com>  
  
RUN apt-get update && apt-get install -y mysql-client  
  
# Download the latest version of magedbm  
RUN curl https://s3-eu-west-1.amazonaws.com/magedbm-releases/magedbm.phar -o
/magedbm.phar  
RUN chmod +x /magedbm.phar  
  
# Add our magedbm wrapper  
COPY magedbm-wrapper.sh /magedbm-wrapper.sh  
RUN chmod +x /magedbm-wrapper.sh  
  
# Allow for magedbm commands to specified  
ENTRYPOINT [ "/magedbm-wrapper.sh" ]  

