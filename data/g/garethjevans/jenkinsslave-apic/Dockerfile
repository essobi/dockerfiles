FROM garethjevans/jenkinsslave:v1.1.5  
RUN apt-get install -y curl npm && \  
npm install -g npm && \  
update-alternatives --install /usr/bin/node node /usr/bin/nodejs 99  
RUN npm install -g apiconnect  
  

