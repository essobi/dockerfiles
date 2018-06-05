FROM codelovers/hhvm-mongo  
  
MAINTAINER Daniel Holzmann <daniel@codelovers.at>  
  
ENV HOME /home/www-data  
ENV TIMEZONE Europe/Vienna  
  
RUN apt-get update && apt-get upgrade -y  
  
# update config  
ADD conf/php.ini /etc/hhvm/php.ini  
ADD conf/server.ini /etc/hhvm/server.ini  
RUN echo date.timezone=$TIMEZONE | tee -a /etc/hhvm/server.ini
/etc/hhvm/php.ini  
  
VOLUME /www  
  
RUN mkdir -p /home/www-data  
ADD run.sh /home/www-data/run.sh  
RUN chown -R www-data:www-data /home/www-data  
RUN chown -R www-data:www-data /home/www-data/run.sh  
  
ENTRYPOINT ["/home/www-data/run.sh"]  
  
EXPOSE 9000  

