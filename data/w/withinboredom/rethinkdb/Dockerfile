FROM withinboredom/consul-agent  
  
MAINTAINER Robert Landers <landers.robert@gmail.com>  
  
# Add the RethinkDB repository and public key  
# "RethinkDB Packaging <packaging@rethinkdb.com>"
http://download.rethinkdb.com/apt/pubkey.gpg  
RUN . /etc/lsb-release && echo "deb http://download.rethinkdb.com/apt
$DISTRIB_CODENAME main" | sudo tee /etc/apt/sources.list.d/rethinkdb.list  
RUN wget -qO- http://download.rethinkdb.com/apt/pubkey.gpg | sudo apt-key add
-  
  
ENV RETHINKDB_PACKAGE_VERSION 2.1.4~0trusty  
  
RUN apt-get update \  
&& apt-get install -y rethinkdb=$RETHINKDB_PACKAGE_VERSION 2>/dev/null \  
&& rm -rf /var/lib/apt/lists/* 2>/dev/null  
  
VOLUME ["/data"]  
  
WORKDIR /data  
  
ADD root /  
  
EXPOSE 28015 29015 8080

