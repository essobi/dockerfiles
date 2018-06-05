FROM ubuntu:xenial  
  
RUN apt-get update -q && \  
apt-get upgrade -qy && \  
apt-get install -qy git-core && \  
apt-get install -qy libxslt1-dev libffi-dev libffi6 libpython-dev libssl-dev
python2.7 python-cherrypy python-lxml python-pip python2.7-dev && \  
apt-get install -qy wget && \  
apt-get clean  
  
RUN pip install pip-review && \  
pip install -U pip pyopenssl ndg-httpsclient virtualenv  
  
RUN git clone https://github.com/CouchPotato/CouchPotatoServer.git
/opt/couchpotato  
  
RUN cd /tmp && \  
wget http://rarlab.com/rar/unrarsrc-5.2.7.tar.gz && \  
tar -xvf unrarsrc-5.2.7.tar.gz && \  
cd unrar && \  
make -f makefile && \  
install -v -m755 unrar /usr/bin  
  
ADD launch.sh /launch.sh  
RUN chmod +x "/launch.sh"  
  
VOLUME ["/data/downloads"]  
VOLUME ["/data/movies"]  
VOLUME ["/data/couchpotato"]  
  
EXPOSE 5050  
CMD ["/launch.sh"]  

