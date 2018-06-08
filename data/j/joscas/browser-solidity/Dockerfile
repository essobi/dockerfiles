FROM node  
MAINTAINER "Josep Casals <joscas@gmail.com>"  
# Install dependency packages  
RUN apt-get update && \  
apt-get install -y git-core  
  
# Install browser-solidity  
RUN mkdir -p /usr/src/browser-solidity  
WORKDIR /usr/src/browser-solidity  
  
RUN git clone https://github.com/ethereum/browser-solidity.git . &&\  
git reset --hard 3448ce4be10f894ac6cc278d5ab9ca9131216c0f  
RUN npm install && \  
npm run build  
  
EXPOSE 8080  
CMD ["npm","run","serve"]  

