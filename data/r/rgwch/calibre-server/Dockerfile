FROM debian:latest  
MAINTAINER weirich@elexis.ch  
COPY startup.sh startup.sh  
RUN apt-get -y update && apt-get -y install calibre && mkdir /srv/calibre &&
chmod +x startup.sh  
EXPOSE 80  
CMD ["./startup.sh"]  

