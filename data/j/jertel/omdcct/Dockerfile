FROM debian  
  
WORKDIR /build  
COPY src/ /build/  
RUN apt update && apt install -y make gcc && make  
  
VOLUME /plot  
  
ENTRYPOINT ["/build/plotavx2","-d","/plot"]  

