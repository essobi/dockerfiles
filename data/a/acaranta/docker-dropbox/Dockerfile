FROM ubuntu:14.04  
MAINTAINER arthur@caranta.com  
RUN apt-get update && apt-get install -y psmisc  
ADD https://www.dropbox.com/download?plat=lnx.x86_64 /dropbox.tgz  
RUN tar xfvz /dropbox.tgz && rm /dropbox.tgz  
  
CMD while true ; do echo "Restarting Dropbox Daemon" ;killall -9 /.dropbox-
dist/dropboxd; /.dropbox-dist/dropboxd; done  
#CMD echo "Restarting Dropbox Daemon" ;/.dropbox-dist/dropboxd  

