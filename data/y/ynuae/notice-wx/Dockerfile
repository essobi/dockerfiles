FROM google/nodejs  
  
RUN mkdir /app  
COPY ./app.js /app/  
COPY ./package.json /app/  
COPY ./app /app/app/  
COPY ./config /app/config/  
  
WORKDIR /app  
  
EXPOSE 18080  
CMD npm -g install forever && npm install && npm start

