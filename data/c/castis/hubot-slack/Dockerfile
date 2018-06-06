FROM node:0.10  
# Install base packages  
RUN npm install -g hubot@2.6.0 coffee-script redis  
  
# Create new hubot and setup for slack.  
RUN cd /root && \  
hubot --create myhubot && \  
cd myhubot && \  
npm install hubot-slack --save && \  
npm install underscore xml2js cron emailjs sugar --save && \  
npm install hubot-horse-racing hubot-magnet hubot-google hubot-figlet hubot-
scripts-kor-castis hubot-map-kor --save && \  
npm install && \  
echo '["hubot-horse-racing", "hubot-scripts-kor-castis", "hubot-figlet",
"hubot-google", "hubot-magnet", "hubot-map-kor"]' > external-scripts.json  
  
# Set environment variables  
ENV TZ Asia/Seoul  
ENV HUBOT_JENKINS_URL http://110.35.173.15/jenkins  
ENV HUBOT_JIRA_URL http://110.35.173.15:8080//jira  
ENV REDISTOGO_URL redis://172.17.42.1:6379/hubot  
  
# HTTP Listener port 9009  
ENV PORT 9009  
EXPOSE 9009  
# Add custum scripts  
ADD hubot-scripts.json /root/myhubot/hubot-scripts.json  
  
# Run hubot("-a slack")  
WORKDIR /root/myhubot  
ENTRYPOINT ["/root/myhubot/bin/hubot", "-a", "slack", "-l", "어이"]  
CMD ["-n", "hubot"]  

