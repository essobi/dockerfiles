FROM wrongsides/baseimage  
  
#Install CouchPotato  
RUN apt-get -q update && apt-get install -qy git-core python python-openssl  
RUN git clone https://github.com/RuudBurger/CouchPotatoServer.git  
  
#Add start script  
ADD ./start.sh /start.sh  
  
RUN chmod u+x /start.sh  
  
USER jarvis  
  
CMD ["/start.sh"]  

