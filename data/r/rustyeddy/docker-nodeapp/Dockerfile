FROM node:8  
# XXX NEED to turn these into ENV vars?  
# VOLUME /srv:/srv  
# WORKDIR /srv/apps/docker-nodeapp/app  
VOLUME /srv/apps/docker-nodeapp:/app  
WORKDIR /app  
  
ENV NODE_ENV development  
  
RUN npm install  
RUN apt-get update && apt-get install -y \  
build-essential \  
python \  
git && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
npm i -g nodemon  
  
# TODO: I need to understand ENTRYPOINTS interaction with CMD better  
# CMD bash  
# Nodemon restarts node when server.js or any of it's  
# dependencies change.  
# CMD bash  
CMD ["/app/runapp.sh"]  
  

