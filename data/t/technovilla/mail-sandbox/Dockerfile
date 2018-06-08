FROM debian:jessie  
  
# Set noninteractive mode for apt-get  
ENV DEBIAN_FRONTEND noninteractive  
  
# postfix  
COPY assets/aliases /etc/aliases  
COPY assets/postfix /etc/postfix  
COPY assets/sasl/smtpd.conf /etc/postfix/sasl/smtpd.conf  
COPY assets/sasl/saslauthd-postfix /etc/default/saslauthd-postfix  
COPY assets/mailname /etc/mailname  
  
# apache2  
COPY assets/apache-sandbox.conf /etc/apache2/conf-available/sandbox.conf  
  
# php  
COPY assets/public_html /home/sandbox/public_html  
COPY assets/mailparse.ini /etc/php5/mods-available/mailparse.ini  
  
# mysql  
COPY assets/mysql/emails.sql /home/sandbox/emails.sql  
  
# cron  
COPY assets/mail-purge.sh /home/sandbox/mail-purge.sh  
COPY assets/mail-purge.sh /home/sandbox/http-purge.sh  
  
COPY install.sh /opt/install.sh  
COPY run.sh /opt/run.sh  
  
RUN /opt/install.sh  
  
EXPOSE 80 25  
# Run the application  
CMD ["/opt/run.sh"]  

