FROM python:2.7  
MAINTAINER libcrack <devnull@libcrack.so>  
  
RUN git clone https://github.com/ProgVal/Limnoria.git && \  
cd Limnoria && \  
pip install -r requirements.txt && \  
python ./setup.py install && \  
rm -rf /Limnoria  
  
#ENV SUPYBOT_CHANNELS  
ENV SUPYBOT_HOME /var/supybot  
ENV SUPYBOT_IDENT supybot  
ENV SUPYBOT_NETWORK freenode  
ENV SUPYBOT_NICK supybot  
#ENV SUPYBOT_PASSWORD  
ENV SUPYBOT_PORT 6697  
ENV SUPYBOT_PREFIXES !  
#ENV SUPYBOT_PREFIX_STRINGS  
ENV SUPYBOT_SERVER irc.freenode.net  
ENV SUPYBOT_USER supybot  
ENV SUPYBOT_USE_SSL True  
ENV SUPYBOT_OWNER owner  
ENV SUPYBOT_OWNER_PASS owner  
  
RUN useradd -d /var/supybot/ -m -r -s /usr/sbin/nologin -U supybot  
  
COPY ["start.sh","/usr/local/bin/"]  
  
USER supybot  
  
WORKDIR /var/supybot  
  
CMD ["/usr/local/bin/start.sh", "supybot.conf"]  

