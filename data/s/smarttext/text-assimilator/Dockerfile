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
wget python python-pip python-requests python-django  
#Git/SmartText/Text-Assimilator.json  
#openjdk8.json  
#--  
RUN mkdir -p /Text-Assimilator  
add repos/SmartText/Text-Assimilator/assimilator /Text-Assimilator/assimilator  
add repos/SmartText/Text-Assimilator/Makefile /Text-Assimilator/Makefile  
add repos/SmartText/Text-Assimilator/start_server.sh /Text-
Assimilator/start_server.sh  
add repos/SmartText/Text-Assimilator/requirements.txt /Text-
Assimilator/requirements.txt  
RUN cd /Text-Assimilator/ && make all && pip install -r requirements.txt -U  
#--  
RUN apt-get purge -y --force-yes make wget python-pip  
RUN apt-get purge software-properties-common -y --force-yes  
RUN apt-get -y autoclean  
RUN apt-get -y autoremove  
RUN rm -rf /var/lib/apt/lists/*  
RUN rm -rf /tmp/*  
RUN rm -rf /var/tmp/*  
EXPOSE 8080  
RUN bash -c 'echo -e "#!/bin/bash\ncd /Text-Assimilator && ./start_server.sh
\$@" >> /entrypoint.sh'  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]

