FROM docker/whalesay:latest  
  
RUN git pull && apt-get -y update && apt-get install -y fortunes  
  
CMD /usr/games/fortune -a | cowsay

