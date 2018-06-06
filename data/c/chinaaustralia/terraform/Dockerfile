FROM docker/whalesay:latest  
RUN apt-get -y update && apt-get install -y fortunes && apt-get install -y
nginx  
CMD /usr/games/fortune -a | cowsay  

