FROM httpd:latest  
  
MAINTAINER takeshi.hirosue@bigtreetc.com  
  
ADD porker /usr/local/apache2/htdocs/  
RUN chown root.www-data -R /usr/local/apache2/htdocs/  
  
EXPOSE 80  
CMD ["httpd-foreground"]  

