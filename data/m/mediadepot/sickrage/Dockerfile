FROM mediadepot/base:python  
  
#Create sickrage folder structure & set as volumes  
RUN mkdir -p /srv/sickrage/app && \  
mkdir -p /srv/sickrage/config && \  
mkdir -p /srv/sickrage/data  
  
WORKDIR /srv/sickrage/app  
  
# Install permanent apk packages  
RUN apk --no-cache --update add py-cheetah openssl-dev bash unrar wget curl \  
\--update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/
--allow-untrusted  
  
#start.sh will download the latest version of sickrage and run it.  
ADD ./start.sh /srv/start.sh  
RUN chmod u+x /srv/start.sh  
  
VOLUME ["/srv/sickrage/config", "/srv/sickrage/data"]  
EXPOSE 8081  
CMD ["/srv/start.sh"]  
  

