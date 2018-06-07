# This is a Dockerfile  
# VERSION 1  
# use the ubuntu base image provided by dotCloud  
FROM ubuntu:14.04  
MAINTAINER Nicholas Harding nickharding@fastmail.net  
  
# make sure the package repository is up to date  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository "deb http://uk.archive.ubuntu.com/ubuntu precise main
universe"  
RUN apt-get update  
  
# install perl and modules  
RUN apt-get clean  
RUN apt-get install -y libc6  
RUN apt-get install -y libc6-dev  
RUN apt-get install -y dpkg-dev  
RUN apt-get install -y g++  
RUN apt-get install -y build-essential  
RUN apt-get install -y make  
RUN apt-get install -y perl  
RUN apt-get install -y cpanminus  
  
RUN cpanm -v PerlIO::locale  
RUN cpanm IPC::Open2  
RUN cpanm -v Text::Names  
RUN cpanm YAML::Any  
RUN cpanm Chess::PGN::Parse  
RUN cpanm File::Find::Rule  
RUN cpanm DBD::SQLite  
RUN cpanm Log::Log4perl  
RUN cpanm Log::Dispatch::File  
  
# install sql  
RUN apt-get install -y sqlite3  
  
ADD ./parsePGN.pl /opt/parsePGN.pl  
RUN perl -c /opt/parsePGN.pl  
  
ADD ./settings.yaml /opt/settings.yaml  
  
ENTRYPOINT ["/usr/bin/perl", "/opt/parsePGN.pl"]  

