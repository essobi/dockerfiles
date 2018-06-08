FROM ubuntu:latest  
MAINTAINER m1lk <hmdilham@gmail.com>  
RUN apt-get update && apt-get install -y cowsay fortune  
RUN rm -Rf /var/cache/apt/lists/*  
CMD /usr/games/cowsay -f dragon $(/usr/games/fortune)  

