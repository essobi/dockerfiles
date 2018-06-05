FROM debian:stable  
MAINTAINER Mildred Ki'Lya  
  
RUN echo deb http://apt.afterlogic.com ./ >> /etc/apt/sources.list  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget  
RUN wget -qO - http://apt.afterlogic.com/pubkey.asc | apt-key add -  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y afterlogic-webmail  
RUN echo | afterlogic install  
RUN rm -f /etc/apache2/sites-enabled/000-default  
RUN sed -i \  
-e 's|^Alias .*|DocumentRoot /usr/share/afterlogic|' \  
/etc/apache2/conf.d/afterlogic  
RUN sed -i \  
-e 's|<DBPrefix.*>|<DBPrefix>webmail_</DBPrefix>|' \  
-e 's|<DBHost.*>|<DBHost>mysql</DBHost>|' \  
-e 's|<DBName.*>|<DBName>webmail</DBName>|' \  
-e 's|<DBLogin.*>|<DBLogin>webmail</DBLogin>|' \  
-e 's|<DBPassword.*>|<DBPassword></DBPassword>|' \  
-e 's|<IncomingMailServer.*>|<IncomingMailServer>imap</IncomingMailServer>|' \  
-e 's|<IncomingMailPort.*>|<IncomingMailPort>993</IncomingMailPort>|' \  
-e 's|<IncomingMailUseSSL.*>|<IncomingMailUseSSL>On</IncomingMailUseSSL>|' \  
-e 's|<OutgoingMailServer.*>|<OutgoingMailServer>smtp</OutgoingMailServer>|' \  
-e 's|<OutgoingMailPort.*>|<OutgoingMailPort>465</OutgoingMailPort>|' \  
-e 's|<OutgoingMailUseSSL.*>|<OutgoingMailUseSSL>On</OutgoingMailUseSSL>|' \  
/usr/share/afterlogic/data/settings/settings.xml  
  
# <DBHost>mysql  
# php /usr/share/afterlogic/afterlogic.php install $DB_NAME $DB_USER $DB_PASS  
  
EXPOSE 80  
  
COPY entry.sh /entry.sh  
ENTRYPOINT ["/entry.sh"]  
CMD ["apache2", "-D", "FOREGROUND"]  

