FROM node:latest  
RUN useradd --user-group --create-home --shell /bin/false app &&\  
npm install  
  
ENV HOME=/home/app  
  
USER app  
  
WORKDIR $HOME/test  

