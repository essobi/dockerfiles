FROM node:7.1  
ENV PORT 4001  
RUN apt-get update \  
&& apt-get install -y nodejs npm git git-core \  
&& ln -s /usr/bin/nodejs /usr/bin/node  
  
# Adding sources  
WORKDIR /home/hft  
COPY . /home/hft  
  
RUN cd /home/hft && npm i  
RUN cd /home/hft && mkdir logs  
  
CMD [ "node", "/home/hft/app.js" ]  
  
EXPOSE 4001

