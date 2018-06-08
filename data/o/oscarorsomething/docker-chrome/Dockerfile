# jess/chrome modified for pulseaudio  
FROM jess/chrome  
MAINTAINER OscarOrSomething  
  
ENV PULSE_SERVER unix:/root/pulse/native  
VOLUME /root/pulse/  
  
CMD ["/usr/bin/google-chrome-stable", "--user-data-dir=/data"]  

