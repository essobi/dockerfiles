FROM node:8.9.3  
MAINTAINER Matt Farmer <matt@frmr.me>  
  
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.2.0/dumb-init_1.2.0_amd64  
  
RUN chmod +x /usr/local/bin/dumb-init  
  
RUN apt-get update && \  
apt-get install -y zip unzip && \  
apt-get clean  
  
ENV GHOSTVER 1.22.2  
ADD
https://github.com/TryGhost/Ghost/releases/download/$GHOSTVER/Ghost-$GHOSTVER.zip
/opt  
  
RUN unzip /opt/Ghost-$GHOSTVER.zip -d /opt/ghost  
  
WORKDIR /opt/ghost  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN adduser ghost  
  
RUN chown -R ghost:ghost /opt/ghost  
  
ADD docker-command.sh /opt/docker-command.sh  
  
RUN chown ghost:ghost /opt/docker-command.sh && \  
chmod ugo+x /opt/docker-command.sh  
  
USER ghost  
  
RUN npm install  
  
RUN mv /opt/ghost/content /opt/ghost/content-default && \  
mkdir content  
  
VOLUME /opt/ghost/content  
  
ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]  
  
CMD ["/opt/docker-command.sh"]  
  
EXPOSE 2368  

