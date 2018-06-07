FROM debian:jessie  
  
MAINTAINER Robin Schneider <ypid@riseup.net>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y python-twisted python-irc python-msnlib python-xmpp python-
sleekxmpp git  
  
WORKDIR /src/howie  
RUN git clone \--branch=docker https://github.com/ypid/Howie.git /src/howie  
  
CMD /src/howie/runme.py  

