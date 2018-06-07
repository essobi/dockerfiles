FROM python:3.4  
MAINTAINER Daniel Cheng <j16sdiz@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y -q \  
wget \  
curl \  
git \  
gcc \  
build-essential  
  
RUN git clone https://github.com/tdryer/hangups.git  
RUN cd hangups && python3 setup.py install ; python3 setup.py install  
  
RUN git clone https://github.com/hangoutsbot/hangoutsbot.git  
RUN cd hangoutsbot && pip3 install -r requirements.txt  
  
RUN mkdir /plugins && touch /plugins/.keep  
RUN mkdir /sinks && touch /sinks/.keep  
COPY start.sh /  
  
VOLUME ["/root/.local/share/hangupsbot", "/plugins", "/sinks"]  
WORKDIR /hangoutsbot/hangupsbot  
  
CMD ["/start.sh"]  

