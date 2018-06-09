# RDF Store Importer Docker Container  
#  
# Docker container to import data into RDF stores (currently only [Virtuoso
Opensource](http://virtuoso.openlinksw.com/dataspace/doc/dav/wiki/Main)).  
#  
#  
## Build:  
#  
# docker build -t loader .  
#  
# Create a folder `import/` and insert some RDF files (file format can be ttl,
nt, ...) to import and may a graph file.  
#  
#  
### Run  
#  
# docker run -v $PWD/import:/import_store -e "STORE_1=uri=>http://ip-
addr:8890/sparql user=>dba pwd=>dba" loader  
#  
FROM ubuntu:14.04  
MAINTAINER Simeon Ackermann <s.ackermann@mail.de>  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# install some basic packages  
RUN apt-get clean && apt-get update  
  
# install some basic packages and virtuoso  
RUN apt-get install -y nginx-light libldap-2.4-2 libssl1.0.0 unixodbc
virtuoso-opensource raptor2-utils pbzip2 pigz  
  
ADD import* /  
  
CMD ["/import.sh"]  
  
VOLUME "/import_store"  
  
# expose the HTTP port to the outer world  
EXPOSE 80  

