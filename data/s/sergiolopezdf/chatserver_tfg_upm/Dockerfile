FROM ubuntu:17.10  
RUN apt-get update  
RUN apt-get install curl -y  
RUN apt-get install sudo  
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -  
RUN apt-get install nodejs -y  
RUN apt-get install git unzip -y  
COPY chatServer.zip /  
RUN unzip chatServer.zip  
WORKDIR chatServer/  
RUN npm install  
ENV PORT=4000  
EXPOSE 4000  
CMD npm start

