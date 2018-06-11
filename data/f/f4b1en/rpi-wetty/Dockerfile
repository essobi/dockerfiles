FROM hypriot/rpi-node  
  
RUN [ "cross-build-start" ]  
  
#Install git  
RUN apt-get update && apt-get install -y curl git wget && rm -rf
/var/lib/apt/lists/*  
  
#### Create user test ####  
RUN useradd -d /home/test -m -s /bin/bash test && \  
echo 'test:test' | chpasswd  
  
WORKDIR /app  
  
RUN git clone https://github.com/krishnasrinivas/wetty .  
RUN npm install  
  
RUN [ "cross-build-end" ]  
  
EXPOSE 3000  
CMD node app.js -p 3000

