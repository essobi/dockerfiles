FROM anapsix/alpine-java  
MAINTAINER Pierre LAURENT (plaurent@sbe-online.com)  
ADD crontab.txt /crontab.txt  
COPY ./software/ /home/  
COPY ./jobs/ /jobs/  
  
COPY entry.sh /entry.sh  
RUN chmod 755 /entry.sh  
RUN chmod 755 /jobs/garantie/start.sh  
  
RUN /usr/bin/crontab /crontab.txt  
  
CMD ["/entry.sh"]  

