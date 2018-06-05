FROM debian  
  
RUN apt-get update && apt-get install -y zip wget && apt-get clean  
  
VOLUME ["/world"]  
VOLUME ["/opt/terraria"]  
EXPOSE 7777  
ADD run.sh /  
  
ENTRYPOINT ["./run.sh"]  

