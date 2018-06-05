# Calibre Server Dockerfile Version 0.0.1  
# host data volume mount in the docker start -v
/host/path/to/library:/opt/calibre-library  
FROM fedora:latest  
MAINTAINER levm "av@levm.eu"  
RUN yum update -y  
RUN yum install -y sudo tar libtool-ltdl  
RUN mkdir /opt/calibre  
#ADD http://download.calibre-ebook.com/2.33.0/calibre-2.33.0-x86_64.txz /opt/  
RUN curl -o /opt/calibre.txz http://download.calibre-
ebook.com/2.33.0/calibre-2.33.0-x86_64.txz  
RUN tar xvf /opt/calibre.txz -C /opt/calibre  
RUN mkdir /opt/calibre-library  
ENV LD_LIBRARY_PATH /opt/calibre/lib  
VOLUME /opt/calibre-library  
ENTRYPOINT ["/opt/calibre/calibre-server", "--with-library", "/opt/calibre-
library"]  
EXPOSE 8080  
#EXPOSE 5353  

