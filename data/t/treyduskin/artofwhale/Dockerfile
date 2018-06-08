FROM docker/whalesay:latest  
  
RUN apt-get -y update && apt-get install -y fortunes  
  
# from http://www.de-brauwer.be/wiki/wikka.php?wakka=TheArtOfWar  
ADD http://www.de-brauwer.be/wastebasket/fortunes-taow-1.0.tar.gz ./  
RUN tar xvf ./fortunes-taow-1.0.tar.gz  
RUN cp fortunes-taow-*/taow* /usr/share/games/fortunes/  
  
CMD /usr/games/fortune taow | cowsay  

