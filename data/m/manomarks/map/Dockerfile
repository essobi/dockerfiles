FROM ubuntu:14.04  
RUN sudo apt-get update  
  
RUN sudo apt-get install -y nodejs  
RUN sudo apt-get install -y npm  
  
COPY . /  
  
RUN cd /src; sudo npm install  
  
EXPOSE 8080  
CMD ["nodejs", "/src/index.js"]  
  

