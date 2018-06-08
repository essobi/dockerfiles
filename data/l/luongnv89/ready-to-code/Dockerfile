# For testing some Dockerfile commands  
# Based on Ubuntu:14.04  
FROM ubuntu  
  
MAINTAINER Luong Nguyen, <luongnv89@gmail.com>  
  
ENV RTC_TAG c_cpp  
  
# Update system  
RUN apt-get update -y  
  
# First message  
RUN echo '*********************************\n*\tReadyToCode
environment\n*\tUbuntu: '`uname -a`'\n*\tVersion/Tag:
'$RTC_TAG'\n************************************"'  
  
# Install github - code version control  
RUN apt-get install -y git  
  
# Install vim - editor  
RUN apt-get install -y vim  
  
# Install wget - downloader for Unix terminal  
RUN apt-get install -y wget  
  
# C/C++ environment  
RUN apt-get install -y build-essential gcc cmake make gdb  
  
# Set workspace - where to start working  
WORKDIR workspace/  
  
# ADD  
# Usage: Add [source directory or URL] [destination directory]  
# ADD README.md /mydata/README.md  
# RUN echo "Copied a file"  
# ADD tools/ /tools/  
# RUN echo "Copied a folder"  
# CMD  
# Usage: CMD "application" "argument", "argument"  
# CMD "echo" "I am CMD"  
# ENTRYPOINT  
# Usage: ENTRYPOINT application "argument","argument"  
# ENTRYPOINT echo  
# CMD "Hello docker"  
# ENTRYPOINT echo  
# ENV  
# Usage: ENV key value  
# ENV MYNAME Luong  
# ENV MYEMAIL luongnv89@gmail.com  
# RUN echo $MYNAME  
# RUN echo $MYEMAIL  
# EXPOSE  
# Usage: EXPOSE [port]  
# EXPOSE 8080  
# USER  
# Usage: USER [UID]  
# RUN useradd luongnv89  
# USER luongnv89  
# VOLUME  
# Usage: VOLUME ["/dir_1","dir_2",...]  
#VOLUME ["~/projects","~/Downloads"]  
# WORKDIR  
# Usage: WORKDIR /path  
RUN echo '*********************************\n*\tThe ReadyToCode environment
'$RTC_TAG' is installed sucessfully!'  
RUN echo '\n* git: '`git --version`  
RUN echo '\n* vim: '`vi -version`  
RUN echo '\n* gcc: '`gcc -v`  
RUN echo '\n* make: '`make -v`  
RUN echo '\n* cmake: '`cmake --version`  
RUN echo '\n* gdb: '`gdb --version`  
RUN echo '\n******************************************'  

