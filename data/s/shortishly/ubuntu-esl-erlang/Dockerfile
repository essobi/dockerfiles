FROM ubuntu  
MAINTAINER Peter Morgan <peter.james.morgan@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
wget  
  
RUN wget http://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb  
RUN dpkg -i erlang-solutions_1.0_all.deb  
  
RUN apt-get install -y \  
erlang  

