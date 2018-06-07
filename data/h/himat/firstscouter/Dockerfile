# firstscouter  
# github.com/hi-mat/firstscouter  
# VERSION 0.1.3  
FROM ubuntu:12.04  
MAINTAINER Matthew Ickstadt, matt@icky.pw  
  
EXPOSE 8080  
# Fix dialogs erroring apt-get installs  
ENV DEBIAN_FRONTEND noninteractive  
  
# install git and wget  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get -q update > install.log  
RUN apt-get -q -y install git wget > install.log  
  
# make home director  
RUN mkdir /home/scout  
RUN cd /home/scout  
  
# installs the newest version of Go  
RUN wget -nv https://godeb.s3.amazonaws.com/godeb-amd64.tar.gz  
RUN tar xvzf godeb-amd64.tar.gz  
RUN ./godeb install  
RUN mkdir ./gocode  
ENV GOPATH /home/scout/gocode  
  
# get firstscouter  
RUN go get -race github.com/hi-mat/firstscouter  
  
CMD /home/scout/gocode/bin/firstscouter  
  

