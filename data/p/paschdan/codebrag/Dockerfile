FROM mkroli/codebrag  
  
RUN mkdir /data  
  
ADD application.conf application.conf  
  
ADD entrypoint.sh entrypoint.sh  
RUN chmod +x entrypoint.sh  
  
EXPOSE 8080  
VOLUME /data  
CMD ./entrypoint.sh  

