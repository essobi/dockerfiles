FROM ubuntu:17.10  
  
RUN apt-get update && apt-get install -y build-essential curl git sudo  
RUN groupadd wheel  
RUN printf "\n%%wheel\tALL=(ALL)\tNOPASSWD: ALL\n" >> /etc/sudoers && visudo
-c  
RUN useradd -m worker -g wheel  
  
WORKDIR /home/worker  
USER worker  

