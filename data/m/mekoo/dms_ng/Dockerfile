# To build and run with Docker:  
#  
# $ docker build -t urban-decision-maker .  
# $ docker run -it --rm -p 3000:3000 -p 3001:3001 urban-decision-maker  
#  
FROM node:latest  
  
RUN mkdir -p /udm /home/nodejs && \  
groupadd -r nodejs && \  
useradd -r -g nodejs -d /home/nodejs -s /sbin/nologin nodejs && \  
chown -R nodejs:nodejs /home/nodejs  
  
WORKDIR /udm  
COPY package.json typings.json /udm/  
RUN npm install --unsafe-perm=true  
  
COPY . /udm  
RUN chown -R nodejs:nodejs /udm  
USER nodejs  
  
CMD npm start  

