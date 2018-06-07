# This is a Dockerfile  
# VERSION 1  
# use the ubuntu base image provided by dotCloud  
FROM ubuntu:12.04  
MAINTAINER Nicholas Harding nickharding@fastmail.net  
  
# make sure the package repository is up to date  
#RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get update  
  
# install stockfish  
RUN apt-get clean  
RUN apt-get install -y g++  
RUN apt-get install -y build-essential  
RUN apt-get install -y curl  
RUN apt-get install -y unzip  
RUN apt-get install -y make  
ADD ./stockfish-dd-src.zip /home/stockfish.zip  
RUN unzip /home/stockfish.zip -d /home/  
RUN cd /home/stockfish-dd-src/src/ && make build ARCH=x86-32  
ENV PATH $PATH:/home/stockfish-dd-src/src/  
  
# install perl and modules  
RUN apt-get install -y build-essential  
RUN apt-get install -y perl  
RUN apt-get install -y cpanminus  
RUN cpanm YAML::Any  
RUN cpanm Chess::PGN::Parse  
RUN cpanm Chess::Rep  
RUN cpanm FileHandle  
RUN cpanm IPC::Open2  
RUN cpanm Term::ANSIColor  
RUN cpanm DBD::SQLite  
RUN cpanm Shell::Command  
  
# install sql  
RUN apt-get install -y sqlite3  
  
ADD ./scorePGN.pl /opt/scorePGN.pl  
ADD ./settings.yaml /opt/settings.yaml  
  
ENTRYPOINT ["/usr/bin/perl", "/opt/scorePGN.pl"]  

