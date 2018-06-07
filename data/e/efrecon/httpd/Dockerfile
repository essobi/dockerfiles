FROM efrecon/mini-tcl  
MAINTAINER Emmanuel Frecon <emmanuel@sics.se>  
  
# Install git so we can install the til and fix some  
# pseudo-directories to make the HTTPd happy at start.  
RUN apk add --update-cache git && \  
git clone https://github.com/efrecon/til /opt/til && \  
rm -rf /opt/til/.git && \  
apk del git && \  
rm -rf /var/cache/apk/* && \  
mkdir /opt/til/bin/lib && \  
ln -s /opt/til /opt/til/bin/lib/ && \  
ln -s /usr/lib/tcllib* /opt/til/bin/lib/  
# Expose alternative port and volumes for root and log  
EXPOSE 8080  
RUN mkdir /opt/www && mkdir /opt/log  
VOLUME /opt/www  
VOLUME /opt/log  
VOLUME /opt/data  
  
# New entrypoint! the server itself, nothing else so we can give it  
# options through CMD (or from compose or similar tool)  
ENTRYPOINT ["tclsh8.6", "/opt/til/bin/httpd.tcl", "-root", "/opt/www", "-log",
"/opt/log/access.log"]  

