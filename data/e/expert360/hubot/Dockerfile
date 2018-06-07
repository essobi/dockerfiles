FROM node:5  
ENTRYPOINT ["/home/hubot/hubot/bin/hubot"]  
  
RUN npm install -g yo generator-hubot  
  
RUN useradd -ms /bin/bash hubot  
USER hubot  
  
# Create the directory to contain the Hubot instance  
RUN mkdir -p /home/hubot/hubot  
WORKDIR /home/hubot/hubot  
  
RUN yo hubot --defaults  

