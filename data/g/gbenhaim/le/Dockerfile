FROM debian:wheezy  
  
RUN echo 'deb http://rep.logentries.com/ wheezy main'
>/etc/apt/sources.list.d/logentries.list  
  
RUN gpg --keyserver pgp.mit.edu --recv-keys C43C79AD && gpg -a --export
C43C79AD | apt-key add -  
  
RUN apt-get update  
  
RUN apt-get install python-setproctitle logentries -y  
  
ENTRYPOINT ["le"]  

