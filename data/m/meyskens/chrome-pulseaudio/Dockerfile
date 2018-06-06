FROM jess/chrome  
  
# yeah i know  
USER root  
RUN gpasswd -a chrome audio  
RUN apt-get update && apt-get -y install pulseaudio  
USER chrome  

