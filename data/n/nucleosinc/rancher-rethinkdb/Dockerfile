FROM debian:jessie  
  
MAINTAINER Piotr Zduniak <piotr@zduniak.net>  
  
# Add the RethinkDB repository and public key  
# "RethinkDB Packaging <packaging@rethinkdb.com>"
http://download.rethinkdb.com/apt/pubkey.gpg  
RUN apt-key adv --keyserver keys.gnupg.net --recv-keys
3B87619DF812A63A8C1005C30742918E5C8DA04A  
RUN echo "deb http://download.rethinkdb.com/apt jessie main" >
/etc/apt/sources.list.d/rethinkdb.list  
  
ENV RETHINKDB_PACKAGE_VERSION 2.3.6~0jessie  
  
RUN apt-get update \  
&& apt-get install -y rethinkdb=$RETHINKDB_PACKAGE_VERSION \  
&& rm -rf /var/lib/apt/lists/*  
  
VOLUME ["/data"]  
  
WORKDIR /data  
  
# process cluster webui  
EXPOSE 28015 29015 8080  
RUN apt update && apt install -y curl  
  
COPY assets/db.sh /db.sh  
COPY assets/proxy.sh /proxy.sh  
  
RUN chmod +x /db.sh  
RUN chmod +x /proxy.sh  
  
ENTRYPOINT [ "/db.sh" ]  

