FROM node:6.6  
RUN useradd --user-group --create-home --shell /bin/false app  
ENV HOME=/home/app  
WORKDIR $HOME  
RUN npm install -g angular-cli@1.0.0-beta.28.3 && npm cache clean  
EXPOSE 4200  
EXPOSE 4205  

