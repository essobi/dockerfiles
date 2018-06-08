#  
# Rocketchat Dockerfile  
#  
# https://github.com/  
#  
# Pull base image.  
FROM debian:latest  
  
MAINTAINER hihouhou < hihouhou@hihouhou.com >  
  
# Update & install packages for installing rocketchat  
RUN apt-get update && \  
apt-get install -y curl graphicsmagick build-essential nodejs #npm nodejs  
  
RUN apt-get install -y npm  
  
RUN npm install -g n  
RUN n 0.10.40  
  
#Download Stable version of Rocket.Chat  
RUN curl -L https://rocket.chat/releases/latest/download -o rocket.chat.tgz &&
\  
tar zxvf rocket.chat.tgz && \  
mv bundle Rocket.Chat && \  
cd Rocket.Chat/programs/server && \  
npm install  
  
CMD ["node", "/Rocket.Chat/main.js"]  

