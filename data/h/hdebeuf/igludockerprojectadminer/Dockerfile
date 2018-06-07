FROM adminer:latest  
  
ENV ADMINER_DESIGN nette \  
ADMINER_DEFAULT_SERVER project1_wordpressdb \  
PROJECT_DOMAIN project.iglu.com  
  
ADD adminerinit.sh /usr/local/bin/adminerinit.sh  
USER root  
RUN chmod +x /usr/local/bin/adminerinit.sh  
  
EXPOSE 8080  
ENTRYPOINT [ "/usr/local/bin/adminerinit.sh" ]  
  
CMD [ "php", "-S", "[::]:8080", "-t", "/var/www/html" ]  

