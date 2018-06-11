FROM ubuntu:17.10  
RUN apt-get update  
RUN apt-get install curl -y  
RUN apt-get install sudo  
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -  
RUN apt-get install nodejs -y  
RUN apt-get install git unzip -y  
RUN apt-get install ffmpeg -y  
COPY videoServer.zip /  
RUN unzip videoServer.zip  
WORKDIR videoServer/  
RUN npm install  
ENV PORT=8000  
EXPOSE 8000-8031  
CMD npm start  

