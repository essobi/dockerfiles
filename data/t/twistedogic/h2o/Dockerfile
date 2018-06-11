FROM twistedogic/rstudio  
MAINTAINER twistedogic  
  
RUN apt-get update  
RUN wget http://h2o-release.s3.amazonaws.com/h2o/rel-
mirzakhani/2/h2o-2.8.3.2.zip -O /opt/h2o-2.8.3.2.zip --no-check-certificate  
RUN cd /opt && unzip h2o-2.8.3.2.zip  
ADD ./run.sh /usr/bin/h2o  
RUN chmod +x /usr/bin/h2o  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 54321 58682 8787 8000 22 7777  
CMD ["/usr/bin/supervisord"]  

