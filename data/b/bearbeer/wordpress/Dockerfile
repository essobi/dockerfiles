FROM wordpress:latest  
  
RUN apt-get update && apt-get install -y --no-install-recommends ssmtp  
  
# Change ssmtp settings  
RUN sed -ri -e 's/^(mailhub=).*/\1smtp/' \  
-e 's/^#(FromLineOverride)/\1/' /etc/ssmtp/ssmtp.conf  
  
# Configure php  
RUN echo "sendmail_path=sendmail -i -t" >> /usr/local/etc/php/conf.d/php-
sendmail.ini  

