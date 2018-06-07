FROM brujoand/dockzb  
  
MAINTAINER Anders Brujordet  
  
ENV SERVICE couchpotato  
  
RUN installer apk python && \  
installer -c git "https://github.com/RuudBurger/CouchPotatoServer.git"  
  
CMD [ "python", "/opt/CouchPotatoServer/CouchPotato.py", "--data_dir",
"/config" ]  
  
EXPOSE 5050  

