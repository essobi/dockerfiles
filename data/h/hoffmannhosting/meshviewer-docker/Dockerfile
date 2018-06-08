FROM node:latest  
  
MAINTAINER Stefan Hoffmann <stefan@freifunk-troisdorf.de>  
  
# Install Yarn  
RUN apt-get update && apt-get install -y curl apt-transport-https && \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && apt-get install -y yarn  
  
# Install Grunt  
RUN npm install --global grunt-cli && \  
apt-get install -y ruby ruby-dev && \  
gem install --no-rdoc --no-ri sass -v 3.4.22 && \  
gem install --no-rdoc --no-ri compass  
  
# Build Meshviewer  
#RUN git clone https://github.com/Freifunk-Troisdorf/meshviewer.git
/opt/meshviewer/  
  
#RUN npm install gulp -D && \  
# yarn && \  
# yarn global add gulp-cli  
  
COPY start.sh /  
RUN chmod +x /start.sh  
  
ENTRYPOINT ["/start.sh"]  
#RUN gulp

