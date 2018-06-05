FROM ubuntu:trusty  
  
RUN apt-get update && apt-get install curl -y  
  
ADD downloader.sh /workdir/  
  
WORKDIR /workdir/  
  
CMD /bin/bash downloader.sh  

