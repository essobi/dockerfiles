FROM ubuntu:trusty  
  
RUN apt-get update && apt-get install curl -y  
  
ADD credentials.php /workdir/  
ADD uploader.sh /workdir/  
  
WORKDIR /workdir/  
  
CMD /bin/bash uploader.sh  

