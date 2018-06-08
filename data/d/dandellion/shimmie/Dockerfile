FROM eboraas/apache-php:latest  
MAINTAINER Daniel Olsen  
  
# install libraries required to interact with supported databases  
RUN apt-get update && apt-get -y install php5-pgsql php5-mysql php5-sqlite &&
apt-get clean  
  
# install tools for thumbnailing and extensions, ffmpeg not yet supported  
RUN apt-get install -y imagemagick unzip  
  
EXPOSE 80  
EXPOSE 443

