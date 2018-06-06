FROM debian  
RUN apt-get update  
RUN apt-get install -y wine  
RUN dpkg --add-architecture i386 && apt-get update && apt-get install -y
wine32  
RUN apt-get install -y curl  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -  
RUN apt-get install -y nodejs  
  
ADD package.json package.json  
RUN npm install  
  
ADD RFFBrowser RFFBrowser  
ADD app.js app.js  
  
ENTRYPOINT ["node", "app.js"]  

