# Java Official image base (https://registry.hub.docker.com/_/java/)  
FROM openjdk:8-jre  
MAINTAINER Marcus Collier "dev@mjcollier.id.au"  
# Install php5 (should probably make this a seperate image)  
RUN apt-get update && apt-get install -y php-cli libmediainfo0v5  
  
# Get filebot and install  
RUN wget -O /tmp/filebot.deb
"https://www.filebot.net/download.php?mode=s&type=deb&arch=amd64"; \  
dpkg -i /tmp/filebot.deb; \  
rm /tmp/filebot.deb;  
  
# Add a seperate volume so filebot cache is persistent (performance is not
great otherwise)  
VOLUME /home/docker  
  
# Set up unprivileged user  
RUN useradd -u 1000 -s /bin/bash docker  
USER docker  
ENV HOME /home/docker  
ENV LANG "en_US.UTF-8"  
# Errors in docker.  
#ENV LC_ALL "en_US.UTF-8"  
  
CMD ["/usr/bin/filebot"]  

