# This Dockerfile creates the Docker image of SAGE2.  
  
# FROM Ubuntu  
FROM ubuntu:latest  
  
# MAINTAINER is ishidakazuya  
MAINTAINER ishidakazuya  
  
# Install SAGE2 and dependencies  
RUN apt-get -y update \  
&& apt-get -y upgrade \  
&& apt-get -y install software-properties-common git curl bzip2 \  
&& add-apt-repository -y ppa:jonathonf/ffmpeg-3 \  
&& curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get update \  
&& apt-get -y install ffmpeg ghostscript libnss3-tools libimage-exiftool-perl
imagemagick nodejs ntp tzdata \  
&& git clone https://bitbucket.org/sage2/sage2.git /usr/local/sage2 \  
&& cd /usr/local/sage2 \  
&& npm install --production \  
&& npm run in \  
&& apt-get -y remove curl bzip2 \  
&& apt-get clean  
  
# EXPOSE Port 9090 and 9292  
EXPOSE 9090  
EXPOSE 9292  
  
# CMD is /bin/bash  
CMD /bin/bash  
  

