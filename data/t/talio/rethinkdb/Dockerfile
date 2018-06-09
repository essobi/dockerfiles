FROM debian:wheezy  
MAINTAINER Lee Faris "lee@talio.co"  
RUN apt-get update -y  
RUN apt-get install wget -y  
RUN apt-get install lsb-release -y  
  
RUN echo "deb http://download.rethinkdb.com/apt `lsb_release -cs` main" | tee
/etc/apt/sources.list.d/rethinkdb.list  
RUN wget -qO- http://download.rethinkdb.com/apt/pubkey.gpg | apt-key add -  
RUN apt-get update  
RUN apt-get install rethinkdb=1.15.2~0wheezy -y  
  
# Define mountable directories.  
VOLUME ["/data"]  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["rethinkdb", "--bind", "all"]  
  
# Expose ports.  
# - 8080: web UI  
# - 28015: process  
# - 29015: cluster  
EXPOSE 8080  
EXPOSE 28015  
EXPOSE 29015  

