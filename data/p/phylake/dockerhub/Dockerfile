FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get -y install wget vim  
  
ENV USERNAME phylake  
ENV TEAM 0  
ENV POWER medium  
  
RUN wget --no-check-certificate \  
https://folding.stanford.edu/releases/public/release/fahclient/debian-
testing-64bit/v7.4/fahclient_7.4.4_amd64.deb  
  
# RUN wget --no-check-certificate \  
# https://folding.stanford.edu/releases/public/release/fahcontrol/debian-
testing-64bit/v7.4/fahcontrol_7.4.4-1_all.deb  
RUN dpkg -i --force-depends fahclient_7.4.4_amd64.deb  
  
ADD config.xml /etc/fahclient/config.xml  
  
CMD /usr/bin/FAHClient --config /etc/fahclient/config.xml  

