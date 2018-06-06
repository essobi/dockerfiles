FROM dockerfile/nodejs  
  
MAINTAINER msgodf@gmail.com  
  
# Dependencies for downloading CoffeeChatter  
RUN apt-get install -y wget unzip  
  
# Setup user account  
RUN useradd -ms /bin/bash coffeechatter  
RUN mkdir -p /home/coffeechatter  
ENV HOME /home/coffeechatter  
USER coffeechatter  
  
WORKDIR /home/coffeechatter  
  
# Download CoffeeChatter from GitHub  
RUN wget https://github.com/simonlord/coffeechatter/archive/master.zip  
RUN unzip master.zip  
  
WORKDIR /home/coffeechatter/coffeechatter-master  
  
# Install dependencies  
RUN npm install dustjs-linkedin dustjs-helpers socket.io@0.9 dust-compiler
debug gravatar underscore  
# Compile Dust templates  
RUN mkdir -p public/js/compiled  
RUN npm run dustc  
  
ENTRYPOINT node app.js  

