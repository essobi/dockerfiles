FROM ubuntu  
  
RUN echo 'deb http://archive.ubuntu.com/ubuntu precise main universe' >>
/etc/apt/sources.list  
RUN apt-get -y update  
RUN apt-get -y install g++  
RUN apt-get install -y erlang-dev erlang-manpages erlang-base-hipe erlang-
eunit erlang-nox erlang-xmerl erlang-inets  
  
RUN apt-get install -y libmozjs185-dev libicu-dev libcurl4-gnutls-dev libtool
wget  
  
RUN cd /tmp ; wget http://apache.crihan.fr/dist/couchdb/source/1.5.1/apache-
couchdb-1.5.1.tar.gz  
  
RUN cd /tmp && tar xvzf apache-couchdb-1.5.1.tar.gz  
RUN apt-get install -y make  
RUN cd /tmp/apache-couchdb-* ; ./configure && make install  
  
RUN printf "[httpd]\nport = 5984\nbind_address = 0.0.0.0\n"
>/usr/local/etc/couchdb/local.d/docker.ini  
  
EXPOSE 5984  
VOLUME ["/usr/local/var/lib/couchdb"]  
CMD ["/usr/local/bin/couchdb"]  

