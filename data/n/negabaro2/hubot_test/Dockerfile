FROM node:latest  
  
RUN mkdir /hubot && cd /hubot  
ADD . /hubot  
  
EXPOSE 9999  
WORKDIR /hubot  
  
CMD ["bin/hubot", "--adapter", "slack"]  

