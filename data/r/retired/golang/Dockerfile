FROM ubuntu:14.04  
  
RUN apt-get -qq update  
  
# Install useful packages.  
# git: Used for getting Go dependencies from Git repositories.  
RUN apt-get -qqy install \  
git  
  
ENV HOME /home  
  
# Install and set up Go environment.  
ADD ./GoBinaries/go1.3.linux-amd64.tar.gz /usr/local  
ENV PATH $PATH:/usr/local/go/bin  
  
RUN mkdir -p $HOME/goCode/bin  
RUN mkdir -p $HOME/goCode/pkg  
RUN mkdir -p $HOME/goCode/src  
  
ENV GOPATH $HOME/goCode  
ENV PATH $PATH:$GOPATH/bin  
  
# Some Go web frameworks use the PORT environment variable to determine which
address to bind to.  
ENV PORT 8000  
  
EXPOSE 8000  
  
RUN apt-get -qqy autoremove  
RUN apt-get -qqy clean  
  
ENTRYPOINT /bin/bash  

