FROM ubuntu:latest  
RUN apt-get update && \  
apt-get install deluge-web -y && \  
useradd deluge -m  
USER deluge  
# Run deluge-web once to create config  
RUN deluge-web -f && \  
sleep 1 && \  
pkill deluge-web --signal SIGINT && \  
sleep 1  
VOLUME /home/deluge/.config/deluge  
EXPOSE 8112  
CMD deluge-web  

