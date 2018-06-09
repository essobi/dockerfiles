FROM swapnil18/docker-arm-busybox:latest  
MAINTAINER Swapnil Das <dasswapnil96@gmail.com>  
  
COPY node_exporter /bin/node_exporter  
  
EXPOSE 9100  
USER  nobody  
ENTRYPOINT [ "/bin/node_exporter" ]  

