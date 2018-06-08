FROM ubuntu:xenial  
MAINTAINER Vincent <vincent@zcorrecteurs.fr>  
  
# software-properties-common est requis pour add-apt-repository  
# gettext-base est requis pour envsubst  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
software-properties-common \  
gettext-base  
  
RUN add-apt-repository ppa:builds/sphinxsearch-rel22 \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends sphinxsearch \  
&& rm -rf /var/lib/apt/lists/*  
  
VOLUME "/var/lib/sphinxsearch/data"  
  
COPY sphinx.conf.template /etc/sphinxsearch/  
COPY reindex.sh /usr/local/bin/  
COPY entrypoint.sh /  
  
RUN chmod +x /entrypoint.sh && chmod +x /usr/local/bin/reindex.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["searchd", "--nodetach"]  

