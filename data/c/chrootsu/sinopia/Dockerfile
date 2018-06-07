FROM keyvanfatehi/sinopia  
MAINTAINER Ilya Mochalov <chrootsu@gmail.com>  
USER root  
RUN apt-get -q update && apt-get install -qy paxctl && paxctl -Cm
/usr/local/bin/node  
USER sinopia  

