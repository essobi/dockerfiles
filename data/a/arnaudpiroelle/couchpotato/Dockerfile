FROM arnaudpiroelle/base  
MAINTAINER Arnaud Piroelle  
  
RUN apt-get install -y python  
  
RUN cd / && git clone https://github.com/sarakha63/CouchPotatoServer.git
couchpotato  
  
EXPOSE 5050  
VOLUME ["/data"]  
VOLUME ["/media"]  
  
CMD ["python", "/couchpotato/CouchPotato.py", "--data_dir", "/data"]  

