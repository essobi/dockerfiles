FROM phusion/baseimage:0.9.17  
MAINTAINER mocadnet <mocadnet@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y make  
RUN apt-get install -y subversion  
  
VOLUME /svnrepos  
  
EXPOSE 3690  
CMD /usr/bin/svnserve -d -r /svnrepos && tail -f /var/log/dpkg.log  

