FROM ubuntu:18.04  
  
RUN apt-get update && apt-get -y install \  
emacs-nox \  
org-mode \  
make \  
tj3  
  
RUN mkdir /emacs/  
ADD init-org.el /emacs/  
ADD ox-taskjuggler.el /emacs/  
  
RUN adduser --disabled-password --gecos "" \--uid 1000 developer  
USER developer  
ADD init.el /home/developer/.emacs  
ENV HOME /home/developer  
WORKDIR /home/developer/work  

