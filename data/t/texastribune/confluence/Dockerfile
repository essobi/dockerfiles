FROM debian:jessie  
MAINTAINER tech@texastribune.org  
  
apt-get -yq update  
apt-get -yq upgrade  
  
ADD http://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-5.5.4-x64.bin /confluence.bin  
RUN chmod +x /confluence.bin  
  
ADD response.varfile /  
RUN /confluence.bin -q -varfile /response.varfile  
  
EXPOSE 8090  
VOLUME /var/atlassian  
VOLUME /opt/atlassian/confluence  
  
CMD ["/opt/atlassian/confluence/bin/start-confluence.sh", "-fg"]  

