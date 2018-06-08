FROM ubuntu  
  
MAINTAINER Matthew Schwartz "@schwartz1375"  
VOLUME [ "/data" ]  
  
RUN apt-get update && apt-get -y -q install tcpdump  
  
CMD [ "-C", "1000", "-W", "100", "-v", "-w", "/data/dump" ]  
  
ENTRYPOINT [ "/usr/sbin/tcpdump" ]  

