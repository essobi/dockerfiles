# Parent-Image festlegen  
FROM leibnizrz/wheezy-base:import  
MAINTAINER Christian Simon <simonc@campus.lmu.de>  
  
# Füge Debian Paketquellen hinzu  
ADD ./sources.list /etc/apt/sources.list  
# Update der Paketlisten  
RUN apt-get update  
# Upgrade des Basissystems  
RUN apt-get -y upgrade && apt-get clean  
  
# Installiere Tools  
RUN apt-get -y install vim git procps psmisc wget supervisor nano pwgen tzdata
rsync && apt-get clean  
  
# Setze Zeitzone  
RUN echo "Europe/Berlin" > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata

