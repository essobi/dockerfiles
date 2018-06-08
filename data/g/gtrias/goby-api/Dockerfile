FROM node:8.9  
LABEL maintainer="Òscar Casajuana <oscar@cirici.com>"  
  
COPY . /app  
  
WORKDIR /app  
  
RUN yarn  
  
ENV NODE_ENV production  
  
ENV PORT 3000  
RUN apt update && apt install unzip && apt-get clean  
  
ENTRYPOINT ["npm", "start"]  

