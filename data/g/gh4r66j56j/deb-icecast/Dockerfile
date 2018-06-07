FROM debian:stable  
MAINTAINER Lachlan de Waard <dockerlachlan@dewaard.email>  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y
--install-recommends icecast2 && rm -rf /var/lib/apt/lists/*  
  
ADD status2.xsl /usr/share/icecast2/web/  
ADD icecast.xml /etc/icecast2/  
  
USER icecast2  
  
CMD icecast2 -c /etc/icecast2/icecast.xml  

