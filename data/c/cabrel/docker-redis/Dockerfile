FROM ubuntu:12.10  
RUN apt-get update  
RUN apt-get -qq -y install python-software-properties software-properties-
common  
RUN apt-add-repository -y ppa:chris-lea/redis-server  
RUN apt-get update  
RUN apt-get -qq -y install redis-server  
EXPOSE 6379  
ENTRYPOINT ["/usr/bin/redis-server", "--daemonize", "yes"]  

