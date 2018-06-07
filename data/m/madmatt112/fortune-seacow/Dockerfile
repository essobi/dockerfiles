FROM docker/whalesay:latest  
RUN apt-get -y update && apt-get install -y fortune  
CMD /usr/games/fortune -a | cowsay && echo && echo "Made with love by Matt."  

