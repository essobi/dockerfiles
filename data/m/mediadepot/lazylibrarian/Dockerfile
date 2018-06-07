FROM mediadepot/base:python  
  
#Create lazylibrarian folder structure & set as volumes  
RUN mkdir -p /srv/lazylibrarian/app && \  
mkdir -p /srv/lazylibrarian/config && \  
mkdir -p /srv/lazylibrarian/data  
  
WORKDIR /srv/lazylibrarian/app  
  
# Install permanent apk packages  
RUN apk --no-cache --update add py-cheetah unrar wget curl \  
\--update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/
--allow-untrusted  
  
#start.sh will download the latest version of lazylibrarian and run it.  
ADD ./start.sh /srv/start.sh  
RUN chmod u+x /srv/start.sh  
  
VOLUME ["/srv/lazylibrarian/config", "/srv/lazylibrarian/data"]  
  
EXPOSE 5299  
CMD ["/srv/start.sh"]  

