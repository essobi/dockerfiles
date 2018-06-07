FROM google/dart:1.24.2  
MAINTAINER <SooToop @Team>  
  
## Ensure to install node using a PPA  
## doc : https://www.digitalocean.com/community/tutorials/how-to-install-node-
js-on-debian-8  
RUN cd ~ && \  
curl -sL https://deb.nodesource.com/setup_6.x -o nodesource_setup.sh && \  
bash nodesource_setup.sh && \  
apt-get install -y nodejs && \  
apt-get install -y build-essential  
  
# install Firebase CLI  
RUN npm install -g firebase-tools && \  
npm install -g update-notifier  
  
# init min i dependencies with pub get  
COPY pubspec.yaml /tmp/init_pub_dep/pubspec.yaml  
RUN cd /tmp/init_pub_dep && pub get  

