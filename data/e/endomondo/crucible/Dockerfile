FROM java:8  
MAINTAINER Mads Hvelplund <mads@swissarmyronin.dk>  
  
ENV CRUCIBLE_VERSION 3.7.0  
### Install and configure packages  
RUN apt-get update && apt-get clean  
RUN apt-get install -y openssh-server supervisor unzip wget git  
  
### Download and unzip Crucible  
RUN wget --no-check-certificate -P /opt
http://www.atlassian.com/software/crucible/downloads/binary/crucible-${CRUCIBLE_VERSION}.zip  
RUN cd /opt && unzip crucible-${CRUCIBLE_VERSION}.zip && rm
crucible-${CRUCIBLE_VERSION}.zip && mv fecru-${CRUCIBLE_VERSION} fecru  
  
### Clean  
RUN apt-get -y autoclean  
RUN apt-get -y clean  
RUN apt-get -y autoremove  
  
### Share /opt  
VOLUME ["/opt/"]  
  
### Expose port  
EXPOSE 22 8060  
###  
CMD ["/opt/fecru/bin/fisheyectl.sh", "run"]

