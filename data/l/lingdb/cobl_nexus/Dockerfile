FROM lingdb/cobl:latest  
  
MAINTAINER Jakob Runge <runjak@gmail.com>  
  
LABEL lingdb="cobl_nexus" \  
version="1.1.0" \  
documentation="https://github.com/lingdb/container/wiki/cobl_nexus"  
  
# Getting ready to run:  
WORKDIR /CoBL  
EXPOSE 5000  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod a+x /entrypoint.sh  
ENTRYPOINT /entrypoint.sh  

