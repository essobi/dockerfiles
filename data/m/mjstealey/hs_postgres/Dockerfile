FROM postgres:9.4.7  
MAINTAINER Michael J. Stealey <stealey@renci.org>  
  
RUN apt-get update && apt-get install -y \  
sudo \  
wget  
  
RUN sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt trusty-pgdg
main" >> /etc/apt/sources.list'  
RUN wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc |
sudo apt-key add -  
RUN apt-get update && apt-get install -y \  
postgresql-9.4-postgis-2.1 \  
pgadmin3 \  
postgresql-contrib-9.4  
  
# Cleanup  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 5432  
CMD ["postgres"]  

