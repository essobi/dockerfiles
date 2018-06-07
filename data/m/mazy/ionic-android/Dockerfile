FROM vielasis/android-sdk-lite  
  
RUN apt-get update && \  
apt-get install -y curl git && \  
curl -sL https://deb.nodesource.com/setup_7.x | bash - && \  
apt-get install -y nodejs gradle && \  
npm i -g cordova ionic@2.1.4 gulp bower && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
echo '{ "allow_root": true }' > /root/.bowerrc  

