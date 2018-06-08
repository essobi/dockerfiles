FROM python:2.7  
MAINTAINER Obosob <obosob@riseup.net>  
RUN git clone https://github.com/Supybot/Supybot.git && cd Supybot && git
checkout -b v0.83.4.1 && python ./setup.py install && rm -rf /Supybot  
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

