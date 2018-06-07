FROM ubuntu:trusty  
  
ADD scripts /home/open-falcon/scripts  
  
RUN sh /home/open-falcon/scripts/prepare.sh  
RUN sh /home/open-falcon/scripts/download.sh  
  
RUN sh /home/open-falcon/scripts/dashboard.sh  
RUN sh /home/open-falcon/scripts/portal.sh  
RUN sh /home/open-falcon/scripts/links.sh  
RUN sh /home/open-falcon/scripts/clean.sh  
  
ADD startup.sh /home/open-falcon/scripts/startup.sh  
ADD supervisord.conf /etc/supervisor/supervisord.conf  
  
EXPOSE 8433 6030 5050 1234 8081 6060 5090 9912  
CMD ["/usr/bin/supervisord"]  

