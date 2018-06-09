FROM mvertes/alpine-mongo:3.6.2-0  
MAINTAINER Zadkiel Aslafy-Aharonian <github@aslafy-z>  
  
COPY endpoint.sh init_repl.sh /  
RUN ["chmod", "+x", "/endpoint.sh", "/init_repl.sh"]  
  
VOLUME /data/db  
ENTRYPOINT ["/endpoint.sh"]  

