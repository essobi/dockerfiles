FROM geertbongers/home-user  
MAINTAINER Geert  
  
RUN apt-get update && apt-get install -qy --force-yes git-core python-pip
unrar python-lxml build-essential python-dev libffi-dev libssl-dev  
RUN pip install --upgrade cryptography pyopenssl ndg-httpsclient pyasn1  
RUN git clone https://github.com/RuudBurger/CouchPotatoServer.git /couch-
potato &&\  
mkdir /container-data &&\  
chown -R home_user:home_user /couch-potato &&\  
chown -R home_user:home_user /container-data  
  
VOLUME /container-data  
  
EXPOSE 5050  
USER home_user  
CMD ["--data_dir", "/container-data"]  
ENTRYPOINT ["dockerize", "-stdout", "/container-data/logs/CouchPotato.log",
"-stderr", "/container-data/logs/error.log", "python", "/couch-
potato/CouchPotato.py"]  

