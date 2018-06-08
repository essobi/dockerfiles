FROM tutum/mysql  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get -y install
apache2 libapache2-mod-php5 php5-mysql php5-ldap php5-gd unzip vim  
  
# to change these you have to rebuild the image  
ENV DB_USER ontology  
ENV DB_NAME ontology  
ENV DB_PASS password  
ENV MYSQL_USER admin  
ENV MYSQL_PASS password  
  
# the following can be changed when running the docker via -e, --env or --env-
file  
ENV SERVER_NAME localhost  
ENV OUR_SERVER_PROTOCOL http  
ENV OUR_SERVER_PORT 8080  
ADD ./neologism.conf /etc/apache2/sites-available/neologism.conf  
RUN sed -i "s/__SERVER_NAME__/$SERVER_NAME/g" /etc/apache2/sites-
available/neologism.conf  
ADD
https://github.com/SpazioDati/Neologism/releases/download/0.5.4c/neologism.zip
/tmp/neologism.zip  
RUN unzip /tmp/neologism.zip -d /tmp && mv /tmp/neologism /var/www/neologism  
  
ADD ./settings.php /var/www/neologism/sites/default/settings.php  
  
RUN mkdir -p /var/www/neologism/sites/default/files  
RUN chown -R www-data: /var/www/neologism  
RUN a2dissite 000-default  
RUN a2ensite neologism  
RUN a2enmod rewrite  
  
ADD ./setup.sql /setup.sql  
RUN sed -i -e "s/{{db_user}}/$DB_USER/g" \  
-e "s/{{db_pass}}/$DB_PASS/g" \  
-e "s/{{db_name}}/$DB_NAME/g" \  
/setup.sql  
  
ADD ./start.sh /start.sh  
RUN chmod +x /start.sh  
  
CMD ["/bin/bash", "-c", "/start.sh"]  

