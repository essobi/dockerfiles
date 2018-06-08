FROM node:8.11  
ENV PORT 4041  
RUN apt-get update \  
&& apt-get install -y nodejs npm git git-core \  
&& ln -s /usr/bin/nodejs /usr/bin/node  
  
# Adding sources  
WORKDIR /home/nodeapp/app/  
COPY . /home/nodeapp/app/  
  
RUN cd /home/nodeapp/app/ && npm install  
RUN cd /home/nodeapp/app/ && mkdir logs  
  
CMD [ "node", "/home/nodeapp/app/server.js" ]  
  
EXPOSE 4041

