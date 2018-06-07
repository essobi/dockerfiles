FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y sudo git && rm -rf
/var/lib/apt/lists/*  
COPY . /root/.dotfiles  
WORKDIR /root/.dotfiles  
CMD ./bin/dotfiles  

