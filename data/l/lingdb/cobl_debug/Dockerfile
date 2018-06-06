FROM lingdb/cobl  
  
MAINTAINER Jakob Runge <runjak@gmail.com>  
  
LABEL lingdb="cobl_debug" \  
version="1.1.0" \  
documentation="https://github.com/lingdb/container/wiki/cobl_debug"  
  
# Getting ready to run:  
WORKDIR /CoBL  
EXPOSE 5000  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod a+x /entrypoint.sh  

