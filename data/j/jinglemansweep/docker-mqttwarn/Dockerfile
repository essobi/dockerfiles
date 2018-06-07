FROM python:2.7  
MAINTAINER JingleManSweep <jinglemansweep@gmail.com>  
  
RUN pip install paho-mqtt slacker  
  
WORKDIR /opt/  
RUN git clone https://github.com/jpmens/mqttwarn.git  
  
ADD ./entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
VOLUME /config  
  
CMD /entrypoint.sh  
  

