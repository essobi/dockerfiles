FROM ubuntu:14.04  
MAINTAINER Sam Liu <ontouchstart@gmail.com>  
  
RUN apt-get update -y  
RUN apt-get upgrade -y  
RUN apt-get -y install git man lynx emacs wget curl gcc make inotify-tools  
RUN wget http://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb  
RUN dpkg -i erlang-solutions_1.0_all.deb  
  
RUN wget http://packages.erlang-solutions.com/ubuntu/erlang_solutions.asc  
RUN apt-key add erlang_solutions.asc  
RUN apt-get update -y  
RUN apt-get -y install erlang-base-hipe erlang erlang-dev erlang-manpages
erlang-mode  
  
ADD .emacs .emacs  
ADD . cowboy  
RUN cd cowboy && make docs install-docs  
RUN cd cowboy/examples && make  

