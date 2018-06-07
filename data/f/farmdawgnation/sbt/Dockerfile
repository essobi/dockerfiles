#  
# Sbt Dockerfile  
#  
# https://github.com/dockerize/sbt  
#  
# Pull base image  
FROM dockerize/java:1.7  
MAINTAINER Dockerize "http://dockerize.github.io"  
# Install Sbt  
RUN wget https://dl.bintray.com/sbt/debian/sbt-0.13.5.deb && dpkg -i
sbt-0.13.5.deb  
  
# Define a volume somewhere other than root  
VOLUME ['/usr/data']  
  
# Drop into work directory  
WORKDIR /usr/data  
  
# Default command  
CMD ["sbt"]  

