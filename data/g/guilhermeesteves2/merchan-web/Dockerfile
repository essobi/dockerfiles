FROM node  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app/  
  
# Setando variavel  
ENV HTTPSERVER="TRUE"  
ENV PORT=18201  
ENV URLAPISERVICE="http://10.158.70.79:18203"  
ENV URLAPIBACK="http://10.158.70.79:18202"  
# Install app dependencies  
COPY package.json /usr/src/app/  
  
# Bundle app source  
COPY server.js /usr/src/app  
COPY server /usr/src/app/server  
COPY frontend /usr/src/app/frontend  
COPY certificados /usr/src/app/certificados  
  
RUN npm -y install  
  
EXPOSE 18201  
CMD ["node", "server"]

