FROM ubuntu:latest  
EXPOSE 80  
RUN apt-get update  
RUN apt-get -y install python-software-properties software-properties-common  
RUN apt-get install -y nodejs  
RUN apt-get install -y npm  
RUN npm install -g gulp  
COPY . /ghost/  
WORKDIR /ghost/  
RUN npm install  
RUN gulp bundle  
ENV NODE_ENV production  
CMD npm start  

