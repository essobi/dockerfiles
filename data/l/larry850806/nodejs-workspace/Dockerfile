FROM larry850806/workspace-base  
  
RUN apt-get -y update && \  
# install nodejs dependencies  
apt-get -y install gnupg gnupg2 && \  
\  
# install nodejs and npm  
curl -sL https://deb.nodesource.com/setup_9.x | bash - && \  
apt-get install -y nodejs && \  
\  
# use npm to install yarn  
npm install -g yarn && \  
\  
# clean cache  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
npm cache clean --force  

