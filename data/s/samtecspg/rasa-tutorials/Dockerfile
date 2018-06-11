FROM node:7.4-alpine  
  
RUN apk update \  
&& apk upgrade \  
&& apk add --no-cache bash git openssh  
  
RUN mkdir /rasa-nlu-data  
  
WORKDIR /rasa-nlu-trainer  
  
RUN git clone https://github.com/RasaHQ/rasa-nlu-trainer.git .  
  
RUN npm install \  
&& npm run build \  
&& npm link  
  
EXPOSE 8080  
CMD ["rasa-nlu-trainer", "-p", "8080"]  

