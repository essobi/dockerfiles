FROM mediadepot/base:python  
  
#Create headphones folder structure & set as volumes  
RUN mkdir -p /srv/headphones/app && \  
mkdir -p /srv/headphones/config && \  
mkdir -p /srv/headphones/data/logs && \  
mkdir -p /srv/headphones/data/cache  
  
WORKDIR /srv/headphones/app  
  
# Install permanent apk packages  
RUN apk --no-cache --update add py-cherrypy py-openssl unrar unzip wget curl \  
\--update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/
--allow-untrusted  
  
#start.sh will download the latest version of headphones and run it.  
ADD ./start.sh /srv/start.sh  
RUN chmod u+x /srv/start.sh  
#  
VOLUME ["/srv/headphones/config", "/srv/headphones/data"]  
  
EXPOSE 8181  
CMD ["/srv/start.sh"]  

