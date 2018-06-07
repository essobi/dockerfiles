FROM davidplatt/nodeopencv  
  
ENV STARTPATH /usr/src/app  
WORKDIR $STARTPATH  
ADD package.json package.json  
RUN npm install  
ADD . .  
RUN chmod +x ./wait-for-it.sh  
CMD ["npm","start"]

