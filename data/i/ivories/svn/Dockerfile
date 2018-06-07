FROM debian:jessie  
  
RUN apt-get update  
RUN apt-get install -y make  
RUN apt-get install -y subversion  
RUN rm -rf /var/lib/apt/lists/*  
  
EXPOSE 3690  
CMD /usr/bin/svnserve -d -r /svn && tail -f /var/log/dpkg.log  

