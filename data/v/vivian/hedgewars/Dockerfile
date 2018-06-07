FROM ubuntu  
  
RUN apt-get update -y  
RUN apt-get install -y -q hedgewars  
  
EXPOSE 9000  
CMD []  
ENTRYPOINT ["/usr/lib/hedgewars/bin/hedgewars-server", "-d", "True", "-p",
"9000"]  

