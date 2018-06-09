FROM teemow/npm  
  
RUN sudo mkdir /static  
RUN sudo chown teemow.teemow /static  
  
ADD . /app  
WORKDIR /app  
RUN sudo chown -R teemow.teemow /app  
  
RUN npm install  
  
# Run http server on port 8080  
EXPOSE 8080  
ENTRYPOINT ["node", "index.js"]  

