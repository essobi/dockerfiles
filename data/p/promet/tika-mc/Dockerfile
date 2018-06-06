FROM java:openjdk-8-jdk  
MAINTAINER Lisa Ridley "lisa@prometsource.com"  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get -y install curl git build-essential && \  
  
curl --silent \--location https://deb.nodesource.com/setup_0.10 | bash - && \  
  
apt-get -y install nodejs && \  
  
npm install forever --global && \  
  
git clone
https://ec39369a30b81669590ad63af90ec06649660814@github.com/promet/mcPDFparser.git
/opt/mcPDFparser && \  
  
cd /opt/mcPDFparser && \  
git pull origin master && \  
npm install /opt/mcPDFparser  
  
EXPOSE 9998 8081  
  
CMD ["/usr/bin/forever", "/opt/mcPDFparser/server.js", "-v -p 8081"]  

