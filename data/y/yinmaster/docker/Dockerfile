FROM docker/whalesay:latest  
RUN apt-get -y update && apt-get install -y fortunes  
RUN wget -qO- https://toolbelt.heroku.com/install.sh | sh  
CMD /usr/games/fortune -a | cowsay

