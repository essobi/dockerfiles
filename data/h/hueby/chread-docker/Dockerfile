FROM mongo:latest  
  
RUN apt-get -y update && apt-get -y install curl sudo git  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN apt-get -y update && apt-get -y install nodejs npm  
RUN npm install -g nodemon  

