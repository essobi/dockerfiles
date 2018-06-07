FROM mysql:5.7  
ENV MYSQL_ROOT_PASSWORD Tigrou007 \  
MYSQL_DATABASE default_db \  
WP_MYSQL_DATABASE vitrine_wordpress \  
PS_MYSQL_DATABASE projectsend \  
MYSQL_USER db_user_project_name \  
MYSQL_PASSWORD db_user_project_password \  
MYSQL_PORT_3306_TCP_ADDR=wordpressdb \  
MYSQL_PORT_3306_TCP_PORT=3306 \  
PROJECT_DOMAIN projectdomainurl \  
PROJECT_NAME_WITH_SPACES projectnamewithspaces  
  
ADD wpdatabase.sql /docker-entrypoint-initdb.d  
RUN chmod -R 777 /docker-entrypoint-initdb.d  
  
COPY mysqlinit.sh /mysqlinit.sh  
RUN chmod +x /mysqlinit.sh  
  
EXPOSE 3306  
ENTRYPOINT ["/mysqlinit.sh"]  
  
CMD ["mysqld"]  

