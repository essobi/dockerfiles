FROM lexandro/linux-base  
  
MAINTAINER Robert Stern <lexandro2000@<you know that big search company>.com  
  
RUN apt-get install golang -y && mkdir /gocode; export GOPATH=/gocode && go
get -u github.com/docker/swarm && cp /gocode/bin/swarm /usr/local/bin/swarm  
  
  

