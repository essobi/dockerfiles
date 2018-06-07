FROM docker/whalesay:latest  
MAINTAINER jongsunglee  
RUN apt-get -y update && apt-get install -y fortune  
CMD /usr/games/fortune -a | cowsay  

