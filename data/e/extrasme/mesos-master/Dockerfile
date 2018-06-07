FROM extrasme/mesos  
MAINTAINER tech@extrasme.com  
  
EXPOSE 5050  
COPY *.sh /mesos/  
RUN chmod +x *.sh  
  
ENTRYPOINT ["./start.sh"]  

