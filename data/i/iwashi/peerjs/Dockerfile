FROM ubuntu:14.04  
MAINTAINER Yoshimasa IWASE <iwase.yoshimasa@gmail.com>  
  
RUN apt-get -y update && apt-get install -y nodejs npm  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN npm install -g peer  
  
EXPOSE 9000  
  
ENTRYPOINT ["peerjs"]  
CMD ["--port", "9000", "--key", "peerjs"]  

