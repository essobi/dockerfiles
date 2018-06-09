FROM ubuntu  
  
MAINTAINER Toby Hughes <toby@learnium.net>  
  
# These variables could be overriden to configure Jicofo  
ENV FOCUS_SECRET="oB2cHipt6Ur0eD6E"  
ENV FOCUS_USER_SECRET="QUnF8ByWyqPiHz5r"  
ENV FOCUS_USERNAME="focus"  
ENV XMPP_DOMAIN="jitsi.example.org"  
ENV XMPP_HOST="localhost"  
ENV XMPP_PORT="5275"  
ENV USER_DOMAIN="auth.jitsi.example.org"  
USER root  
RUN apt-get update && apt-get -y install \  
ant \  
git-core \  
unzip \  
default-jdk  
  
RUN git clone https://github.com/jitsi/jicofo.git  
  
RUN cd /jicofo && ant dist.lin64  
  
ADD scripts/run.sh /run.sh  
  
CMD ["/run.sh"]  

