FROM wiredthing/oraclejdk:7u72  
MAINTAINER Doug Clinton <doug@wiredthing.com>  
  
WORKDIR /root  
RUN apt-get install -y unzip  
RUN wget -q http://downloads.typesafe.com/play/1.2.5.3/play-1.2.5.3.zip  
RUN unzip -q play-1.2.5.3.zip  
RUN mv play-1.2.5.3 /opt/play  
RUN rm play-1.2.5.3.zip  
  
RUN apt-get install -y python  
  
RUN useradd -m play  
RUN chown -R play /opt/play  
RUN chgrp -R play /opt/play  
  
WORKDIR /home/play  
  
USER play  
  
EXPOSE 9000  

