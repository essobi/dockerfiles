# Play Framework 2.2.1 for Ubuntu 13.10  
#  
# Version 0.1  
FROM pulse00/scala  
MAINTAINER Robert Gruendler r.gruendler@dubture.com  
  
# Get dependencies  
RUN apt-get install -y --force-yes unzip  
  
# Get play  
RUN cd /opt && wget http://downloads.typesafe.com/play/2.2.3/play-2.2.3.zip &&
unzip play-2.2.3.zip && rm /opt/play-2.2.3.zip  
  
# Set path  
ENV PLAYPATH /opt/play-2.2.3  
ENV PATH $PLAYPATH:$PATH  
  
# Define default command.  
CMD ["play"]  

