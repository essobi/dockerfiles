from php:7.0-apache  
ARG GIT_REPO_URL  
RUN apt-get update && apt-get install -y git  
  
COPY gitclone /usr/local/bin/  
RUN chmod a+x /usr/local/bin/gitclone  
  
EXPOSE 80  
CMD ["gitclone", "apache2-foreground"]  
  

