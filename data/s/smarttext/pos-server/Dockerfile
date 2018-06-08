FROM ubuntu:14.04  
MAINTAINER Varun Mittal <vaurn91@uw.edu>  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
RUN apt-get update  
RUN apt-get install -y --force-yes --no-install-recommends software-
properties-common apt-transport-https  
RUN add-apt-repository -y 'ppa:openjdk-r/ppa'  
RUN apt-get -y update --allow-unauthenticated  
RUN apt-get install -y --force-yes --no-install-recommends openjdk-8-jdk make
wget unzip  
#Git/SmartText/POS-Server.json  
#openjdk8.json  
#--  
RUN mkdir -p /pos-server  
add repos/SmartText/POS-Server/src /pos-server/src  
add repos/SmartText/POS-Server/javax /pos-server/javax  
add repos/SmartText/POS-Server/Makefile /pos-server/Makefile  
add repos/SmartText/POS-Server/start_server.sh /pos-server/start_server.sh  
RUN cd /pos-server/ && make all  
#--  
RUN apt-get purge -y --force-yes make wget unzip  
RUN apt-get purge software-properties-common -y --force-yes  
RUN apt-get -y autoclean  
RUN apt-get -y autoremove  
RUN rm -rf /var/lib/apt/lists/*  
RUN rm -rf /tmp/*  
RUN rm -rf /var/tmp/*  
EXPOSE 8080  
RUN bash -c 'echo -e "#!/bin/bash\ncd /pos-server && ./start_server.sh \$@" >>
/entrypoint.sh'  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]

