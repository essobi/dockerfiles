#  
# Hubot-rocketchat Dockerfile  
#  
# https://github.com/  
#  
# Pull base image.  
FROM debian:latest  
  
MAINTAINER hihouhou < hihouhou@hihouhou.com >  
  
# Update & install packages for installing rocketchat  
RUN apt-get update && \  
apt-get install -y git curl && \  
useradd hubot -m  
  
RUN curl -sL https://deb.nodesource.com/setup | bash - && \  
apt-get install -y nodejs  
  
#Download Stable version of Rocket.Chat  
RUN git clone https://github.com/RocketChat/hubot-rocketchat.git && \  
cd hubot-rocketchat && \  
npm install -g coffee-script yo generator-hubot  
  
USER hubot  
RUN cd /home/hubot/ && \  
mkdir myhubot && \  
cd myhubot && \  
yo hubot -f --no-insight --owner="Hihouhou <hihouhou@hihouhou.com>"
\--name="hihouhou" \--description="Bot" \--adapter="rocketchat"  
  
WORKDIR /home/hubot/myhubot/  
  
CMD ["./bin/hubot", "-a", "rocketchat"]  

