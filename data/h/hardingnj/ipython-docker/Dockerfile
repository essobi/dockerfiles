FROM ubuntu:14.04  
MAINTAINER Nicholas Harding <njh@well.ox.ac.uk>  
  
RUN apt-get install -y curl  
RUN apt-get update  
RUN curl -O
https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda3-2.2.0-Linux-x86_64.sh  
RUN bash Anaconda3-2.2.0-Linux-x86_64.sh -b  
RUN apt-get install -y python-qt4  
  
EXPOSE 8888  
ADD ./notebook.sh /notebook.sh  
ENTRYPOINT ["/bin/bash", "notebook.sh"]  

