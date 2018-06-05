FROM ubuntu:trusty  
ENV REFRESHED_AT 20151113  
RUN apt-get update && \  
apt-get install curl -y && \  
curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash - && \  
apt-get install nodejs -y && \  
npm install -g npm && \  
npm install -g yo generator-hubot && \  
useradd -m hubot && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
USER hubot  
RUN cd ~ && echo 'n' | yo hubot --adapter=slack --owner="Patrik Antonsson
<patant@gmail.com>" \--name="bot" \--description="The BOT" && \  
npm install hubot-devopsreactions --save && \  
npm install hubot-cute-me --save && \  
npm install hubot-curl --save && \  
npm install hubot-beer-me --save  
WORKDIR /home/hubot  
COPY external-scripts.json ./external-scripts.json  
CMD ./bin/hubot --adapter slack  

