FROM ubuntu  
  
MAINTAINER Elizandro Pacheco <elizandro@nexthop.net.br>  
  
WORKDIR /  
  
RUN apt-get update \  
&& apt-get install -y wget  
  
RUN wget http://install.speedtest.net/ooklaserver/ooklaserver.sh  
RUN chmod a+x ooklaserver.sh  
RUN ./ooklaserver.sh install -f  
  
EXPOSE 8080  
EXPOSE 5060  
#CMD ["./OoklaServer"]  

