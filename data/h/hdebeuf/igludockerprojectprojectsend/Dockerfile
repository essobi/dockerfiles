FROM linuxserver/projectsend:80  
  
ENV MYSQL_DATABASE_HOST=project_mysqldb \  
PS_MYSQL_DATABASE=projectsend \  
MYSQL_USER=db_user_project_name \  
MYSQL_PASSWORD=db_user_project_password \  
PROJECT_DOMAIN=projectdomainurl \  
PROJECT_NAME_WITH_SPACES=projectnamewithspaces \  
WEBMASTER_LOGIN=webmaster \  
WEBMASTER_PASSWORD=Tigrou007  
  
RUN rm /defaults/sys.config.php  
ADD init-config.php /etc/cont-init.d/init-config.php  
RUN chmod +x /etc/cont-init.d/init-config.php  
  
ADD fileserverinit.sh /fileserverinit.sh  
RUN chmod +x /fileserverinit.sh  
  
EXPOSE 80  
  
ENTRYPOINT ["/fileserverinit.sh"]  

