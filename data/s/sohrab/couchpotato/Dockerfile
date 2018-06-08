FROM debian:wheezy  
MAINTAINER sohrab <sohrab.hosseini@gmail.com>  
  
WORKDIR /opt  
RUN apt-get update && \  
apt-get install -y \  
git-core \  
python && \  
git clone https://github.com/RuudBurger/CouchPotatoServer.git && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME /volumes  
  
EXPOSE 5050  
COPY start.sh /  
RUN chmod +x /start.sh  
CMD ["/start.sh"]

