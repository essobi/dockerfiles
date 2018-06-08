FROM previousnext/base:latest  
MAINTAINER Nick Schuch <nick@previousnext.com.au>  
  
RUN apt-get -qq update && apt-get -y upgrade && apt-get clean  
  
RUN apt-get install -y ruby1.9.1-dev libsqlite3-dev build-essential  
RUN gem install mailcatcher --no-ri --no-rdoc  
  
##  
# Supervisord.  
##  
ADD ./conf/supervisor/supervisord.conf /etc/supervisord.conf  
  
##  
# Startup scripts.  
##  
ADD ./scripts/start.sh /root/start.sh  
RUN chmod 755 /root/start.sh  
  
EXPOSE 1080  
EXPOSE 25  
  
CMD ["/root/start.sh"]  

