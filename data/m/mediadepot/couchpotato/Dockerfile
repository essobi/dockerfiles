FROM mediadepot/base:python  
  
#Create couchpotato folder structure & set as volumes  
RUN mkdir -p /srv/couchpotato/app && \  
mkdir -p /srv/couchpotato/config && \  
mkdir -p /srv/couchpotato/data  
  
WORKDIR /srv/couchpotato/app  
  
# Install permanent apk packages  
RUN apk --no-cache --update add libffi-dev py-lxml openssl-dev py-cherrypy
unrar unzip wget curl \  
\--update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/
--allow-untrusted && \  
pip install pyopenssl ndg-httpsclient  
  
#start.sh will download the latest version of couchpotato and run it.  
ADD ./start.sh /srv/start.sh  
RUN chmod u+x /srv/start.sh  
#  
VOLUME ["/srv/couchpotato/config", "/srv/couchpotato/data"]  
  
EXPOSE 5050  
CMD ["/srv/start.sh"]  

