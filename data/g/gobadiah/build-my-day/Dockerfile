FROM debian  
  
RUN apt-get update -y  
  
RUN apt-get install -y vim curl sudo aptitude  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN sudo apt-get install -y nodejs  
  
COPY . /root/src  
  
WORKDIR /root/src  
  
RUN NODE_ENV=production npm install  
  
EXPOSE 3000  
CMD node index.js  

