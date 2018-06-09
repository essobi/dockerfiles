FROM odise/busybox-node  
  
# Install base packages  
RUN npm install -g hubot coffee-script yo redis-server generator-hubot  
RUN npm install hubot-cute-me hubot-thank-you hubot-business-cat hubot-victory
hubot-thesimpsons hubot-calculator hubot-hearthstone hubot-euphemism --save  
  
RUN adduser -D myhubot; \  
echo "myhubot ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
ENV HOME /home/myhubot  
  
# Create new hubot and setup for slack.  
RUN mkdir -p /home/myhubot && \  
cd /home/myhubot && \  
yo hubot --adapter="slack" \--name="taliobot" \--defaults && \  
npm install hubot-slack --save  
  
ADD external-scripts.json /home/myhubot/external-scripts.json  
# HTTP Listener port 9009  
ENV PORT 9009  
EXPOSE 9009  
# Run hubot("-a slack")  
WORKDIR /home/myhubot  
ENTRYPOINT ["/home/myhubot/bin/hubot", "-a", "slack"]  
CMD ["-n", "taliobot"]  

