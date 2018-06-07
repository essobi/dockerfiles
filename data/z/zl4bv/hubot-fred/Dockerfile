FROM node  
MAINTAINER Ben Vidulich <ben@vidulich.co.nz>  
  
RUN useradd -d /hubot -m -s /bin/bash -U hubot  
  
WORKDIR /hubot  
USER hubot  
  
COPY bin/ /hubot/bin/  
COPY external-scripts.json /hubot/  
COPY package.json /hubot/  
COPY scripts/ /hubot/scripts/  
  
CMD bin/hubot --adapter slack  

