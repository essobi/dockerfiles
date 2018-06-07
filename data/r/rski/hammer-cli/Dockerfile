FROM ubuntu:trusty  
MAINTAINER Romanos Skiadas <rom.skiad@gmail.com>  
  
RUN echo "deb http://deb.theforeman.org/ trusty stable" >
/etc/apt/sources.list.d/foreman.list && sudo apt-get update && sudo apt-get
install wget -y && wget -q https://deb.theforeman.org/foreman.asc -O- | apt-
key add -  
RUN sudo apt-get update && sudo apt-get install -y ruby-hammer-cli ruby-
hammer-cli-foreman vim-tiny  

