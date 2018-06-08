FROM ubuntu  
  
RUN apt-get update && apt-get install -y haproxy  
  
ENTRYPOINT [ "haproxy", "-f" ]  
  
CMD [ "/etc/haproxy/haproxy.cfg" ]  

