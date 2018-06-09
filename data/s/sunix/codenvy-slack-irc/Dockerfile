FROM codenvy/shellinabox  
  
EXPOSE 3000  
ENV CODENVY_APP_PORT_3000_HTTP 3000  
  
RUN sudo apt-get update && \  
sudo apt-get upgrade -y && \  
sudo apt-get install -y patch nodejs node-gyp nodejs-legacy npm && \  
sudo npm install -g slack-irc  

