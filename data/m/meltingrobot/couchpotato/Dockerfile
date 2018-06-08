# Version 0.0.1  
FROM fedora:latest  
MAINTAINER Roy P "meltingrobot@gmail.com"  
RUN dnf -y update  
RUN dnf -y install git python2  
RUN pip install --upgrade pyopenssl  
RUN git clone https://github.com/CouchPotato/CouchPotatoServer.git
/opt/couchpotato  
CMD [ "/bin/python", "/opt/couchpotato/CouchPotato.py" ]  
VOLUME /opt/couchpotato  
EXPOSE 5050  

