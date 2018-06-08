FROM node:6.7.0-slim  
  
RUN wget -O /wait-for-it.sh https://raw.githubusercontent.com/iturgeon/wait-
for-it/8f52a814ef0cc70820b87fbf888273f3aa7f5a9b/wait-for-it.sh \  
&& chmod +x /wait-for-it.sh  
  
COPY package.json /src/  
WORKDIR /src/  
RUN npm install  
  
ADD . /src/  
  
CMD node /src/script.js  

