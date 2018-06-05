FROM ubuntu:14.04  
MAINTAINER Shane Logsdon <shane@shanelogsdon.com>  
  
RUN apt-get update  
RUN apt-get install -y curl  
RUN curl http://mirror.racket-
lang.org/installers/6.0.1/racket-6.0.1-x86_64-linux-ubuntu-precise.sh >
racket.sh  
RUN echo "yes\n1\n" | /bin/bash racket.sh  
RUN rm racket.sh  

