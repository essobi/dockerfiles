FROM node:boron  
  
#Install bower  
RUN npm install --global bower  
RUN npm install --global polymer-cli  
  
#Create APP folder  
RUN mkdir -p /usr/src/app  
  
#Set workdir app  
WORKDIR /usr/src/app  
  
#Install dependencies  
COPY webapp/bower.json /usr/src/app  
RUN bower install --allow-root  
  
#Package APP  
COPY webapp/ /usr/src/app/  
  
#Expose port and run  
EXPOSE 8081  
#CMD [ "polymer","serve --hostname 0.0.0.0" ]  
ENTRYPOINT ["polymer", "serve"]  
CMD ["--hostname", "0.0.0.0"]  

