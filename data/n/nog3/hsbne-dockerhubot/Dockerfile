FROM google/nodejs  
  
MAINTAINER nog3 (nog3@nog3.net)  
  
RUN npm install -g yo generator-hubot  
RUN npm install -g coffee-script  
RUN npm install hubot -g  
RUN echo "Australia/Brisbane" | tee /etc/timezone  
RUN dpkg-reconfigure --frontend noninteractive tzdata  
  
RUN useradd hubot -m -s /bin/bash  
ENV HOME /home/hubot  
USER hubot  
WORKDIR /home/hubot  
  
RUN yo hubot --owner="HSBNE (executive@hsbne.org)" \--name="HSBNEBot"
\--description="HSBNE Chatbot" \--adapter=irc --defaults  
RUN npm install hubot-diagnostics hubot-youtube hubot-url-title hubot-help
hubot-tell hubot-seen hubot-podbaydoors hubot-dinner hubot-substitute hubot-
old hubot-suggest hubot-loudbot hubot-bikeshed hubot-react --save  
ADD external-scripts.json /home/hubot/  
  
ENV HUBOT_IRC_SERVER irc.freenode.net  
ENV HUBOT_IRC_ROOMS #hsbne  
ENV HUBOT_IRC_NICK HSBNEBot  
  
  
  
CMD /home/hubot/bin/hubot --adapter irc  
  

