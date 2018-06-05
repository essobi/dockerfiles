FROM debian:stretch  
  
RUN apt-get update  
RUN apt-get install -y dialog  
RUN apt-get install -y --no-install-recommends rsyslog logrotate  
RUN apt-get install -y libglib2.0-data shared-mime-info xdg-user-dirs libhttp-
message-perl liblog-dispatch-perl libipc-shareable-perl  
RUN apt-get install -y apache2 libapache2-mod-fcgid libcgi-fast-perl  
RUN apt-get install -y --no-install-recommends munin  
RUN apt-get install -y munin-doc  
  
ADD ./munin.conf /etc/apache2/sites-available/munin.conf  
  
RUN a2enmod rewrite  
RUN a2enmod fcgid  
RUN a2dissite 000-default.conf  
RUN a2ensite munin  
  
RUN sed -i 's/LogLevel warn/LogLevel info/g' /etc/apache2/apache2.conf  
RUN sed -i 's/Listen 80/Listen 8080/g' /etc/apache2/ports.conf  
RUN sed -i 's/Alias \/munin \/var\/cache\/munin\/www/#Alias \/munin
\/var\/cache\/munin\/www/g' /etc/munin/apache24.conf  
RUN sed -i 's/\\[localhost.localdomain\\]/#\\[localhost.localdomain\\]/g'
/etc/munin/munin.conf  
RUN sed -i 's/address 127.0.0.1/#address 127.0.0.1/g' /etc/munin/munin.conf  
RUN sed -i 's/use_node_name yes/#use_node_name yes/g' /etc/munin/munin.conf  
  
ADD ./start-munin.sh /munin  
  
EXPOSE 8080  
CMD ["bash", "/munin"]  

