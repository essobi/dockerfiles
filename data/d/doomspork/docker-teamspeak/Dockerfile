# TeamSpeak 3  
#  
# VERSION 1.0.0  
FROM ubuntu:vivid  
MAINTAINER James Brink, brink.james@gmail.com  
  
# Setup needed dependencies  
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*  
  
# Download TeamSpeak 3  
RUN mkdir /app && curl
"http://dl.4players.de/ts/releases/3.0.11.3/teamspeak3-server_linux-
amd64-3.0.11.3.tar.gz" | tar xfvz - -C /app --strip-components=1 && touch
/runSetup  
  
# Copy any docker assets into container  
COPY ./assets /local/opt/docker-assets/  
RUN chmod -R 775 /local/opt/docker-assets  
  
# Expose needed ports for TeamSpeak  
# Default voice port (UDP in): 9987  
EXPOSE 9987  
# Default filetransfer port (TCP in): 30033  
EXPOSE 30033  
# Default serverquery port (TCP in): 10011  
EXPOSE 10011  
# Default tsdns port (TCP in): 41144  
EXPOSE 41144  
CMD ["/local/opt/docker-assets/bin/teamspeak.sh"]  

