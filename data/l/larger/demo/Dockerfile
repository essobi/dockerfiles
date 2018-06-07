FROM ubuntu:16.04  
RUN apt-get update && \  
apt-get -y install curl && \  
apt-get -y install xfce4-panel && \  
echo ""  
  
WORKDIR /app  
COPY startup.sh .  
RUN chmod +x startup.sh  
CMD ["/app/startup.sh"]

