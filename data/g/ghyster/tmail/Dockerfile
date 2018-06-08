# tmail docker file  
FROM toorop/tmail  
MAINTAINER Nicolas Le Gras <nicolas.legras@gmail.com>  
  
USER tmail  
  
WORKDIR /home/tmail/dist/  
  
RUN . conf/tmail.cfg && \  
./tmail user add -r tmail tmailpasswd  
  
EXPOSE 2525  
  
CMD ["/home/tmail/dist/run"]  

