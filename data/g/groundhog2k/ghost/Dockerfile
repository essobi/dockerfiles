FROM debian:latest  
MAINTAINER Goeran Poehner "goeran.poehner@gmail.com"  
LABEL Description="Ghost blog"  
  
RUN apt-get update && apt-get upgrade -y && apt-get install wget tar jq sudo
python make procps -y  
WORKDIR /  
  
RUN mkdir -p /opt/nodejs && wget
https://nodejs.org/dist/v6.14.2/node-v6.14.2-linux-x64.tar.gz && tar xvf
node-v6.14.2-linux-x64.tar.gz -C /opt/nodejs --strip-components 1  
RUN ln -s /opt/nodejs/bin/node /usr/bin/node && ln -s /opt/nodejs/bin/npm
/usr/bin/npm  
ENV PATH=$PATH:/opt/nodejs/bin  
RUN npm i -g ghost-cli  
RUN useradd -m ghost-www  
RUN mkdir /opt/ghost && chown ghost-www:ghost-www /opt/ghost  
WORKDIR /opt/ghost  
USER ghost-www  
RUN ghost install --production --no-stack --db sqlite3 --url
http://localhost:2368 --ip "0.0.0.0" \--port 2368 --no-start --process "local"
\--no-prompt  
  
COPY scripts/start.sh /usr/local/bin  
RUN tar cvf content.tar content  
  
VOLUME /opt/ghost/content  
EXPOSE 2368  
ENTRYPOINT ["/usr/local/bin/start.sh"]  

