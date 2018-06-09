FROM ubuntu:16.04  
RUN apt-get update --fix-missing  
RUN apt-get install -y libxrender1  
RUN apt-get install -y libxtst6  
RUN apt-get install -y libxi6  
RUN apt-get install -y libgtk2.0-0  
RUN apt-get install -y libcanberra-gtk-module  
RUN apt-get install -y git  
  
ENV ARCHIVE WebStorm-2017.2.tar.gz  
  
ADD https://download.jetbrains.com/webstorm/$ARCHIVE /  
  
RUN tar xvzf $ARCHIVE  
  
VOLUME /root  
VOLUME /projects  
  
CMD ["/WebStorm-172.3317.70/bin/webstorm.sh"]  

