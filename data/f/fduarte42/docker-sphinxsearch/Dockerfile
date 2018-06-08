FROM ubuntu:16.04  
  
RUN apt-get update && apt-get upgrade -y && apt-get install -y sphinxsearch
wget php7.0-cli php7.0-xmlreader php7.0-zip  
  
RUN mkdir /var/www  
RUN mkdir /var/www/html  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod u+x /entrypoint.sh  
  
VOLUME ["/var/lib/sphinxsearch/data"]  
  
EXPOSE 9312 9306  
  
ENTRYPOINT ["/entrypoint.sh"]  
  

