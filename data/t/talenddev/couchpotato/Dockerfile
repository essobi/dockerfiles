FROM talenddev/python  
MAINTAINER talenddev <leo@talenddev.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN git clone https://github.com/RuudBurger/CouchPotatoServer.git
/opt/CouchPotatoServer  
  
# Add couchpotato to runit  
RUN mkdir /etc/service/CouchPotato  
ADD start.sh /etc/service/CouchPotato/run  
RUN chmod +x /etc/service/CouchPotato/run  
  
EXPOSE 5050  

