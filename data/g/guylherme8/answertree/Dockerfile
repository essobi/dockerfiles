FROM node  
RUN npm install -g gulp jshint  
#create app directory  
RUN mkdir -p /usr/src/answerTree  
WORKDIR /usr/src/answerTree  
  
COPY package.json /usr/src/answerTree  
RUN npm install  
  
COPY . /usr/src/answerTree  
  
EXPOSE 8080  
CMD ["gulp"]  

