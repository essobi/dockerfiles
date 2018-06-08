  
FROM mirkokiefer/ubuntu-base  
  
RUN apt-get update  
  
# couch deps  
RUN apt-get install -y g++ build-essential  
RUN apt-get install -y erlang-dev erlang-manpages erlang-base-hipe erlang-
eunit erlang-nox erlang-xmerl erlang-inets  
# couch dev deps  
RUN apt-get install -y libmozjs185-dev libicu-dev libcurl4-gnutls-dev libtool  
  
RUN curl http://mirrors.gigenet.com/apache/couchdb/source/1.5.0/apache-
couchdb-1.5.0.tar.gz > /tmp/apache-couchdb-1.5.0.tar.gz  
ADD scripts /scripts  
RUN bash /scripts/install_couch.sh  
  
ADD local.ini /usr/local/etc/couchdb/local.ini  
  
EXPOSE 5984  
CMD ["couchdb"]  
  

