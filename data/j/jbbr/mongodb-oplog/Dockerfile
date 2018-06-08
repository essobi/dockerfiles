FROM mvertes/alpine-mongo:3.2.10-3  
MAINTAINER Janek Thomaschewski  
  
RUN apk add --no-cache mongodb-tools  
  
COPY repl_init.sh run.sh /root/  
RUN chmod +x /root/*.sh  
  
ENTRYPOINT /root/run.sh  
CMD mongod  

