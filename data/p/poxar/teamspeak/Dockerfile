  
#  
# teamspeak  
#  
# Builds a basic docker image that can run TeamSpeak  
# (http://teamspeak.com/).  
#  
FROM debian:stable  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -qqy update \  
&& apt-get -qqy upgrade \  
&& apt-get -qqy install curl  
  
# Download and install TeamSpeak 3  
RUN curl
"http://teamspeak.gameserver.gamed.de/ts3/releases/3.0.11.2/teamspeak3-server_linux-
amd64-3.0.11.2.tar.gz" -o teamspeak3-server_linux-amd64.tar.gz  
RUN tar zxf teamspeak3-server_linux-amd64.tar.gz  
RUN mv teamspeak3-server_linux-amd64 /opt/teamspeak  
RUN rm teamspeak3-server_linux-amd64.tar.gz  
  
# Load in config files  
ADD start /start  
ADD ts3server.ini /etc/ts3server.ini  
  
# Fix permissions  
RUN chmod +x /start  
  
# /start runs it.  
EXPOSE 9987/udp  
EXPOSE 10011  
EXPOSE 30033  
VOLUME ["/data"]  
CMD ["/start"]  
  

