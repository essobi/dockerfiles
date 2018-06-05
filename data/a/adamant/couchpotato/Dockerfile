FROM alpine:3.6  
MAINTAINER Adam Dodman <adam.dodman@gmx.com>  
  
ENV UID=901 GID=900  
WORKDIR /couchpotato  
  
ADD start.sh /start.sh  
  
RUN chmod +x /start.sh \  
&& apk add --no-cache tini su-exec python2 py2-openssl py2-lxml openssl unrar
tar git \  
&& git clone https://github.com/CouchPotato/CouchPotatoServer.git /couchpotato
\  
&& apk del --no-cache git  
  
VOLUME ["/config", "/media"]  
EXPOSE 5050  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD ["/start.sh"]  

