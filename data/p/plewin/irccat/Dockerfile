FROM ubuntu  
MAINTAINER Philippe Lewin <philippe.lewin@gmail.com>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y git python python-
setuptools python-twisted  
  
RUN mkdir -p /opt/irccat/config  
RUN cd /opt/irccat && git clone https://github.com/JustinAzoff/python-irccat  
RUN cd /opt/irccat/python-irccat && python setup.py install  
  
ENTRYPOINT ["irccat", "/opt/irccat/config/irccat.ini"]  
  
VOLUME ["/opt/irccat/config"]  
EXPOSE 5000  

