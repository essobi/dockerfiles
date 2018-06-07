FROM httpd  
  
MAINTAINER J.W. Volschenk <jwvolschenk@gmail.com>  
  
ENV SITE_VERION="1.0.0"  
COPY ./UI/ /usr/local/apache2/htdocs/  
  
#Add start script  
RUN mkdir -p /opt/credo  
  
ADD run.sh /opt/credo  
  
RUN chmod +x /opt/credo/run.sh  
  
CMD ["/opt/credo/run.sh"]  
  

