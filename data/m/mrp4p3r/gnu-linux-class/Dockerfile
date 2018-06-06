FROM ubuntu  
  
RUN apt update && apt install -y make gcc  
  
COPY ./src/ /src/  
  
RUN cd /src && make clean && make install && mkdir -p /lab5/log  
  
WORKDIR /src  
  
CMD lab5  

