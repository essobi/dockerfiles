FROM learninglayers/base  
  
MAINTAINER Dominik Renzel  
  
RUN apt-get update  
RUN apt-get install -y \  
wget \  
unzip  
  
WORKDIR /var/www  
  
RUN wget http://layers.dbis.rwth-
aachen.de/jenkins/job/MobSOS%20Surveys/lastSuccessfulBuild/artifact/*zip*/archive.zip  
RUN unzip archive.zip  
WORKDIR /var/www/archive  
RUN mv ./webapp /var/www/surveys-frontend  
WORKDIR /var/www  
RUN rm -rf archive archive.zip  
WORKDIR /var/www/surveys-frontend  
  
VOLUME ["/var/www/surveys-frontend/"]  

