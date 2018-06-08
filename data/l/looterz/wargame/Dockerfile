FROM f69m/ubuntu32:trusty  
MAINTAINER Looter Loots  
RUN apt-get update && apt-get install -y wget nano  
WORKDIR /home  
RUN wget https://87.98.143.182:10281/dedicated/wargame3_server.tar.bz2 --no-
check-certificate  
RUN tar xvjf wargame3_server.tar.bz2  
WORKDIR /home/wargame3_server  
RUN chmod 755 wargame3-server  
ENTRYPOINT ["/home/wargame3_server/wargame3-server"]  

